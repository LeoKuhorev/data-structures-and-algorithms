def reverse_array(lst):

    output = []
    for _ in range(len(lst)):
        output.append(lst.pop())
    return output
