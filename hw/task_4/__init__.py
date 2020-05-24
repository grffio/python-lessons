def masquerade(val: str):
    """
    Function which masquerade some sensitive value:
        - masquerade all data except for the 2 first and 2 last symbols;
        - not be masquerade if the value contain only numbers and its length is <= to 6;
        - not be masquerade first and last symbol if the value contain chars and numbers and it length <= 4.
    """
    if type(val) != str:
        print(f"invalid type, expected 'string'")
        return

    arr = list(val)
    arr_len = len(arr)

    # Check that all elements in the array are numbers.
    all_number = False
    for item in arr:
        if not item.isdigit():
            all_number = False
            break
        all_number = True

    if all_number:
        if arr_len <= 6:
            return val

    if arr_len <= 4:
        return masquerade_elem(arr, arr_len, 1)

    return masquerade_elem(arr, arr_len, 2)


def masquerade_elem(arr: list, arr_len: int, num: int):
    """
    Replace elements in the array with '*' between the number at the beginning and at the end.
    """
    for i in range(1, arr_len):
        last = arr_len + 1 - num
        if i <= num or i >= last:
            continue
        arr[i - 1] = "*"

    return ''.join(arr)
