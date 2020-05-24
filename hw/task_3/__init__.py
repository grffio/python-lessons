def max_num_parser(val: str):
    """
    Function which accepts parameter s - string, of a format "number;number;number".
    The functions should parse this string and return maximum number.
    """
    if type(val) != str:
        print(f"invalid type, expected 'string'")
        return

    num_arr = val.split(";")
    for item in num_arr:
        num_format = item.replace('.', '').replace('-', '')
        if not num_format.isdigit():
            print(f"invalid item type: '{item}', expected number in 'float' or 'int'")
            return

    num_arr.sort()
    max_num = num_arr[len(num_arr) - 1]

    return to_number(max_num)


def to_number(val: str):
    """
    Function that converts value to number.
    """
    num = 0
    err_int = False

    try:
        num = int(val)
    except ValueError:
        err_int = True
    if err_int:
        try:
            num = float(val)
        except ValueError:
            print(f"failed convert to number: '{val}', unexpected error")
            return

    return num
