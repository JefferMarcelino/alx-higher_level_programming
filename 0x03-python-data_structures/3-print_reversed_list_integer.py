#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """A function that prints all integers of a list, in reverse order

    Args:
        my_list: the list

    Return:
        Nothing
    """
    if not my_list:
        pass
    else:
        idx = len(my_list) - 1

        while idx >= 0:
            print("{:d}".format(my_list[idx]))
            idx -= 1
