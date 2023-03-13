#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """A function that replaces an element in a list at a
    specific position without modifying the original list

    Args:
        my_list: the list
        idx: the given position
        element: the new element

    Return:
        The new list
    """
    if len(my_list) - 1 < idx or idx < 0:
        return (None)
    new_list = my_list[:]
    new_list[idx] = element
    return (new_list)
