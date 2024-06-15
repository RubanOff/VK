# merge sort without additional array
# len(arr1_with_zeros) = len(arr1) + len(arr2)

def merge(arr1, arr2):
    pointer1 = len(arr1) - len(arr2) - 1
    pointer2 = len(arr2) - 1
    pointer3 = len(arr1) - 1

    while pointer2 >=0:
        if pointer1 >=0 and arr1[pointer1] > arr2[pointer2]:
            arr1[pointer3] = arr1[pointer1]
            pointer1 -=1
        else:
            arr1[pointer3] = arr2[pointer2]
            pointer2 -=1
        pointer3 -=1

    return arr1
    
with open("/Users/eugene/Desktop/VK education/Семинар №1/test_4.txt") as file:
    for  counter , i in file:
        if counter % 2 == 0:
            arr1 = list(map(int, i.split()))
        if counter % 2 == 1:
            arr2 = list(map(int, i.split()))
            print(arr1, arr2, end= )

