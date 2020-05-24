def char_counter(val: str):
    """
    Function which accepts parameter s - string, and returns
    dictionary d with keys being letters in that word, and value being the
    count of the letter in the string.
    """
    if type(val) != str:
        print(f"invalid type, expected 'string'")
        return

    dct = {}
    arr = list(val)
    for item in arr:
        dct[item] = arr.count(item)

    return dct
