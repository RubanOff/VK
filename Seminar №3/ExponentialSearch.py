# Экспоненциальный поиск

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

target = 12

def binarySearch(array, left, right, target):

    if len(arr) == 0:
        return print("Введите коректный массив!")
    

    if left > right:
        return False
    
    middle = int((right + left) // 2)

    if array[middle] == target:
        return middle
    
    if array[middle] > target:
        return binarySearch(array, left, middle - 1, target)
    else:
        return binarySearch(array, middle + 1, right, target)

def exponentialSearch(array, target):
    border = 1
    LastElem = len(array) - 1


    while border < LastElem and array[border] < target:
        border = border * 2

        if border > LastElem:
            border = LastElem


        if array[border] == target:
            return border
        
        
    return binarySearch(array, border/2, border, target)
    

print(exponentialSearch(arr, target))


