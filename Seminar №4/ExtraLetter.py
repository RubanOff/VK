# Find the difference between two strings

def extra_letter(a, b):

    # Create a dictionary(hash -_-)
    hash_map_a = {}
    

    # Fill in hash_map_a
    for char in a:
        if char in hash_map_a:
            hash_map_a[char] += 1
        else:
            hash_map_a[char] = 1

    # Checking the existence of a letters
    for char in b:
        if char in hash_map_a:
            hash_map_a[char] -= 1
            if hash_map_a[char] == 0:
                del hash_map_a[char]
        else:
            return char
    
    
    return ""

print(extra_letter('uiokjbk', 'oeiu'))


# Тесты
with open("Семинар №4/test_ExtraLetter.txt") as file:
    for counter, i in enumerate(file):
        if counter % 2 == 0:
            arr1 = str(list(map(str, i.split())))
        if counter % 2 == 1:
            arr2 = str(list(map(str, i.split())))
            print(arr1, arr2, end = " <-----> ")
            print(extra_letter(arr1, arr2))
        
        
