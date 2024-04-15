#!/usr/bin/python3
'''Module for Mylist class with print_sorted as method.'''


class MyList(list):
    '''my local MyList class.'''
    def print_sorted(self):
        '''Method with the sorted function to print out the sorted list.'''
       sorted_lists = sorted(self)
       print(sorted_lists)
