special_array = [1, 2, [3, 2], 6, [[2, 3], 1], 7]

def get_sum_elements_of_special_array(array, depth=1):
    result = 0

    for element in array:
        if isinstance(element, list):
            result += get_sum_elements_of_special_array(element, depth + 1) 
        else:
            result += element
    return result * depth

print(get_sum_elements_of_special_array(special_array))