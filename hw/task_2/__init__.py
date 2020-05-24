def pop_div2(val: list):
    """
    Function which accepts parameter l - list of object of any nature,
    removes all the numbers, divisible by 2 (without a reminder) from
    that list, and returns it.
    """
    if type(val) != list:
        print(f"invalid type, expected 'list'")
        return

    for item in val:
        if type(item) == int:
            if (item % 2) == 0:
                index = val.index(item)
                val.pop(index)

    return val
