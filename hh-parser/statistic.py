class Statistic():
    """ Class to create statistics """
    def __init__(self, vacancies):
        """ Initiate counters for displaying statistics """
        self.vacancies = vacancies
        self.employers = 0
        self.processed = 0
        self.suitable = 0
        self.unsuitable = 0

    def show_stat(self):
        """ Print all statistics """
        print('')
        println('Total vacancies:', self.vacancies)
        println('Total employers:', self.employers)
        println('Processed      :', self.processed)
        println('Suitable       :', self.suitable)
        println('Unsuitable     :', self.unsuitable)
        print('')

    def set_employers(self, employers):
        """ Set employers counter """
        self.employers = employers

    def up_processed(self):
        """ Increase processed counter """
        self.processed += 1
    
    def up_suitable(self):
        """ Increase suitable counter """
        self.suitable += 1

    def up_unsuitable(self):
        """ Increase unsuitable counter """
        self.unsuitable += 1

def println(string, count):
    """ Print readable line """
    print(string + ' ' + str(count))