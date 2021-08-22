list_of_numbers = [1, 2, 3, 4, 5, 6, 7]

def sum_of_numbers_with_sum(ll):
    return sum(ll)

def sum_of_numbers_with_recursion(ll):
    result = 0
    i = len(ll) - 1
    if len(ll) <= 0:
        return 0
    result += ll[i] + sum_of_numbers_with_recursion(ll[:-1])
    
    return result

sum_result = sum_of_numbers_with_sum(list_of_numbers)

recursion_result = sum_of_numbers_with_recursion(list_of_numbers)

print(f"Result usinng sum is:{sum_result}")
print("-----------")
print(f"Result using recursion is:{recursion_result}")
