#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """A function that prints all integers of a list, in reverse order

    Args:
        my_list: the list

    Return:
        Nothing
    """
    for idx in range(1, len(my_list) + 1):
        print("{:d}".format(my_list[idx * -1]))
