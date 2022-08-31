from typing import List


def join(*lists, sep='-') -> List:
    """
    Join lists with seperator.
    :param lists: lists of lists
    :param sep: seperator operator between list.
    :return: join list.
    """

    list_of_all = []
    for index, lst in enumerate(lists):
        list_of_all += [item for item in lst]
        if len(lists) > 1 and index < len(lists) - 1:  # to separate lists
            list_of_all.append(sep)
    return list_of_all


# Tests
if __name__ == '__main__':
    print(join([1, 2], [8], [9, 5, 6], sep='@'))
    print(join([1, 2], [8], [9, 5, 6]))
    print(join([1]))
    print(join())
