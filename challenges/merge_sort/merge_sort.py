def merge(L: list, R: list, lst: list) -> list:
    i = j = k = 0

    while i < len(L) and j < len(R):

        if L[i] < R[j]:
            lst[k] = L[i]
            i += 1
        else:
            lst[k] = R[j]
            j += 1
        k += 1

    if i < len(L):
        lst[k:] = L[i:]
    elif j < len(R):
        lst[k:] = R[j:]

    return lst


def merge_sort(lst: list) -> list:
    _len = len(lst)

    if _len > 1:
        mid_idx = _len // 2
        L = lst[0: mid_idx]
        R = lst[mid_idx:]

        merge_sort(L)
        merge_sort(R)
        
        merge(L, R, lst)

    return lst


lst = [2, 4, 6, 7, 8, 4, 2, 5, 7]

print(merge_sort(lst))
