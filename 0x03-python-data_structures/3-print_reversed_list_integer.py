#!/usr/bin/python3
# This function prints the integers in a list in reverse order
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    for n in reversed((my_list)):
        print('{:d}'.format(n))
