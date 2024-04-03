#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for r in range(list_length):
        try:
            result = my_list_1[r] / my_list_2[r]
        except IndexError:
            print("out of range")
            result = 0
        except ZeroDivisionError:
            print("divison by 0")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        finally:
            result_list.append(result)
    return result_list
