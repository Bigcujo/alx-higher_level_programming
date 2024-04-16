#!/usr/bin/python3
'''Module for Mylist class.'''


class MyList(list):
    '''Custom Mylist class.'''
    def print_sorted(self):
        '''This prints out the list in a sorted manner'''
        sorted_lists = sorted(self)
        print(sorted_lists)
