word = "Basics"

def recursive_string(word, i = 0):
    new_word = ""
    if i == len(word):
        return ""
    
    new_word += word[i] + recursive_string(word, i + 1)
   
    return new_word

print(recursive_string(word))
        
