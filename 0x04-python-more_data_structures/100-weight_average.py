def weight_average(my_list=[]):
    if not my_list:
        return 0
    
    numerate = 0
    denominate = 0
    
    # Iterate through each tuple in the list
    for weight, value in my_list:
        # Calculate the numerator by adding the product of weight and value
        numerate += weight * value
        # Calculate the denominator by adding the weight
        denominate += weight
    
    # Calculate and return the weighted average
    if denominate != 0:
        return numerate / denominate
    else:
        return 0  # Avoid division by zero
