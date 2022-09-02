from typing import List


def join(*lists, seperator_character='-') -> List:
    """
    Join lists with seperator.
    :param seperator_character: seperator operator between list.
    :param lists: lists of lists
    :return: join list.
    """

    list_of_all = []
    for index, lst in enumerate(lists):
        list_of_all += [item for item in lst]
        if len(lists) > 1 and index < len(lists) - 1:  # to separate lists
            list_of_all.append(seperator_character)
    return list_of_all


if __name__ == '__main__':
    print(join([1, 2], [8], [9, 5, 6], seperator_character='@'))
    print(join([1, 2], [8], [9, 5, 6]))
    print(join([1]))
    print(join())
