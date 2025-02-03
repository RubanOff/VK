# Find an anagrams in an array and combine it into nested arrays

def group_anagrams(data):
    # Create a dictionary
    hash_map = {}
    
    for word in data:
        # Sorted words that can help find anograms()
        sorted_word = ''.join(sorted(word))
        if sorted_word in hash_map:
            # Add to the beginning
            hash_map[sorted_word].insert(0, word)
        else:
            hash_map[sorted_word] = [word]


    output = hash_map.values()
    return output
    

# Tests
with open("Семинар №4/test_Anagram.txt") as file:
    for cl in file:
        input = list(map(str, cl.split()))
        print(input, end='<----->')
        print(group_anagrams(input))