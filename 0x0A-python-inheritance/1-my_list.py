'''Module for MyList class.'''

class MyList(list):
    '''A custom subclass of the built-in list class.'''
    
    def print_sorted(self):
        '''Prints the elements of the list in sorted order.'''
        sorted_list = sorted(self)
        print(sorted_list)
