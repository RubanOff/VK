from ClassTree import buildTree
# Function that calculate Min * Max multiplication binary tree

def max_min_multiplication(data):
    if len(data) < 3:
        return -1
    
    min_index = 1
    max_index = 2

    # Left node
    i = 1
    while i < len(data):
        min_index = i
        i = 2 * i + 1

    # Right node
    i = 1
    while i < len(data):
        max_index = i
        i = 2 * i + 2

    result = data[min_index] * data[max_index]
    return result

# Test
data = [3, 5, 2, 7, 4, 8, 9]
buildTree(data)
print("\nMaximum and minimum multiplication:")
print(f"Max * Min = {max_min_multiplication(data)}")