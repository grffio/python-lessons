import requests
import json
import sys

from statistic import Statistic

vacancy_name = 'devops'
key_words = ['inc']

# Api documentation: https://github.com/hhru/api/blob/master/docs/vacancies.md#search
base_url_api = 'https://api.hh.ru/'
base_url_hh = 'https://hh.ru/employer/'
query_vacancies = f'vacancies/?area=1&period=30&per_page=100&text={vacancy_name}'
query_employers = 'employers/'


def do_request(url):
    """
    Return response from the provided URL.
    """
    r = requests.get(url)

    # Warn and exit if 'Status Code' not 'OK 200'
    if r.status_code != 200:
        print('Error, Status Code: ' + str(r.status_code))
        sys.exit()
    return r


def get_vacancies(url):
    """
    Get all vacancies data from the provided URL.
    """
    vacancies = []
    resp = do_request(url)

    # Append 'vacancies' with data from zero page
    vacancies.append(json.loads(resp.text))

    # Set new statistics value of vacancies
    found_vacancies = vacancies[0]['found']
    stat = Statistic(found_vacancies)

    # Pagination, go through all available pages if response had more than one page
    pages = int(vacancies[0]['pages'])
    if pages > 0:
        for page in range(1, pages):
            resp = do_request(url + '&page=' + str(page))
            # Append 'vacancies' with data from the current page
            vacancies.append(json.loads(resp.text))
    return vacancies, stat


def get_employers_ids(vacancies, stat):
    """
    Go through all the vacancies and take the ID of the employer.
    """
    employers_ids = []

    # We need to go through the array many times since its structure is 'vacancies[page]items[vacancy]'
    for page in vacancies:
        for item in page['items']:
            # Easily eliminate duplicates IDs,
            # continue work and skip employers without ID
            try:
                employer_id = item['employer']['id']
                if employer_id not in employers_ids:
                    employers_ids.append(employer_id)
            except KeyError:
                continue

    # Set new statistics value of employers
    stat.set_employers(len(employers_ids))

    return employers_ids


def sort_employer(url, employer, keywords, stat):
    """
    Fetch description about the employer and parse it by keywords.
    """
    resp = do_request(url+employer)

    # Increase the processed value of the statistic
    stat.up_processed()

    description = json.loads(resp.text)['description']
    return parse_employer(description, keywords, stat)


def parse_employer(description, keywords, stat):
    """
    Check for keywords in the employer's description.
    """
    for kw in keywords:
        # Go to the next one if the given employer has no description
        try:
            result = description.lower().find(' ' + kw)
        except AttributeError:
            break

        if result != -1:
            stat.up_suitable()
            return True

        stat.up_unsuitable()
        return False


def main():
    """
    Display links to those employers whose keywords are in the description.
    """
    vacancies, stat = get_vacancies(base_url_api + query_vacancies)
    employers_ids = get_employers_ids(vacancies, stat)

    for employer_id in employers_ids:
        status = sort_employer(base_url_api + query_employers, employer_id, key_words, stat)
        if status:
            print(base_url_hh + employer_id)

    stat.show_stat()


if __name__ == "__main__":
    main()
