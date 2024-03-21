#!/usr/bin/python3
def search_replace(my_list, search, replace):
    #this will be for the update list
    new_list = []
#this will go through the loop to find the element 
    for value in my_list:
        if value == search:
            new_list.append(replace)
        else:
            new_list.append(value)
    return new_list


