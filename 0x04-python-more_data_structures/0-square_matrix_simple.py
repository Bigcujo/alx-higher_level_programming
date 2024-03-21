#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    #creating an empty matrix to store the answer
    result_matrix = []

    #nested for loop
    for rows in matrix:
        #create a new row for new matrix
        result_rows = []

        for elements in rows:
            result_rows.append(elements ** 2)
        result_matrix.append(result_rows)
    return result_matrix    
