# Четные вперед 

def evenFirst(arr):
    pointer = 0
    for i in range(len(arr)):
        if(arr[i] % 2 == 0):
            arr[i], arr[pointer] = arr[pointer], arr[i]
            pointer += 1

        
    return arr

with open("/Users/eugene/Desktop/VK education/Семинар №1/test_1.txt") as file:
    for cl in file:
        inpt = list(map(int, cl.split()))
        print(inpt, end='<----->')
        print(evenFirst(inpt))