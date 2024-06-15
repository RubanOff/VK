# Все нули вперед 

def swapnull(arr):
    pointer = len(arr) - 1
    for i in reversed(range(len(arr))):
        if arr[i] == 0:
            arr[pointer], arr[i] = arr[i], arr[pointer]
            pointer -= 1

    return arr

with open("/Users/eugene/Desktop/VK education/Семинар №1/test_6.txt") as file:
    for i in file:
        inpt = list(map(int, i.split()))
        print(inpt, end = "<----->")
        print(swapnull(inpt))
