


# def get_subsiquence(word):
#     if len(word) == 0:
#         return ""

#     first_part = word[0]
#     rest = get_subsiquence(word[1:])

#     result = ""
#     for substring in rest.split(","):
#         result += "," + first_part + substring
#         result += "," + substring
#     result = result[1:]
    
#     return result

# print(get_subsiquence("XYZ"))

def get_subsiquence(word):
    if len(word) == 0:
        return ""

    first_part = word[0]
    rest = get_subsiquence(word[1:])

    result = ""
    for substring in rest.split(","):
        result += "," + first_part + substring
        result += "," + substring
    result = result[1:]
    
    return result

print(get_subsiquence("XYZ"))