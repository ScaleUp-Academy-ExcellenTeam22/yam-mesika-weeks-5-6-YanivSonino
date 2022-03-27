

def join(*lists, sep='-'):
    if not lists:
        return None

    list_of_all = []
    for lst in lists:
        for item in lst:
            list_of_all.append(item)
        if len(lists) > 1:  # to separate lists
            list_of_all.append(sep)
    return list_of_all


# Tests
print(join([1, 2], [8], [9, 5, 6], sep='@'))
print(([1, 2], [8], [9, 5, 6]))
print(join([1]))
print(join())