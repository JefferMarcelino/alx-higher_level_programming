#!/usr/bin/python3
def element_at(my_list, idx):
    """A function that retrieves an element on the list
    at a given index

    Args:
        my_list: the list
        idx: the given index

    Return:
        The element at the given index, otherwise None
    """
    if len(my_list) - 1 < idx or idx < 0:
        return (None)
    return (my_list[idx])
