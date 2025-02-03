#merge sort with additional array

def merge_sorted_arrays(arr1, arr2):
    merged_array = list()
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i = i + 1
        else:
            merged_array.append(arr2[j])
            j = j + 1
    
    merged_array.extend(arr1[i:])
    merged_array.extend(arr2[j:])


    return merged_array


# Тесты
with open("/Users/eugene/Desktop/VK education/Семинар №1/test_2.txt") as file:
    for counter, i in enumerate(file):
        if counter % 2 == 0:
            arr1 = list(map(int, i.split()))
        if counter % 2 == 1:
            arr2 = list(map(int, i.split()))
            print(arr1, arr2, end = "<----->")
            print(merge_sorted_arrays(arr1, arr2))
