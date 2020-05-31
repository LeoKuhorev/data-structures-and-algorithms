def reverse_array(lst):
    """Function that reverses a given array

    Arguments:
        lst {lst} -- Python list

    Returns:
        lst -- Python list
    """
    output = []
    for _ in range(len(lst)):
        output.append(lst.pop())
    return output
