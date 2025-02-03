# Правый бинарный поиск (поиск последнего вхождения)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 12]
target = 10

def rightBinarySearch(arr, target):

    if len(arr) == 0:
        return print("Введите коректный массив!")
    
    left = 0
    right = len(arr) - 1
    result = -1
    
    while left <= right:
        middle = left + (right - left) // 2
        
        if arr[middle] == target:
            result = middle
            left = middle + 1
        elif arr[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    
    return result


print(rightBinarySearch(arr, target))