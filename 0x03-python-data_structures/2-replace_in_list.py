#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """A function that replaces an element of a list at a specific position

    Args:
        my_list: the list
        idx: the specific position
        element: the new element

    Return:
        The modified list, otherwise the original
    """
    if len(my_list) - 1 < idx or idx < 0:
        return (my_list)
    my_list[idx] = element
    return (my_list)
