def swap_dict(val: dict):
    """
    Function which return swapped key and values in a dictionary.
    """
    if type(val) != dict:
        print(f"invalid type, expected 'dict'")
        return

    new_dict = {}
    for v in val:
        new_key = val.get(v)
        new_dict[new_key] = v

    return new_dict
