# Бинарный поиск (рекурсивно)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,]

target = 12
left = 0
right = len(arr) - 1


def binarySearch(array, left, right, target):

    if len(arr) == 0:
        return print("Введите коректный массив!")

    if left > right:
        return False
    
    middle = (left + right) // 2

    if array[middle] == target:
        return middle
    
    if array[middle] > target:

        return binarySearch(array, left, middle - 1, target)
    else:
        return binarySearch(array, middle + 1, right, target)
    

print(binarySearch(arr, left, right, target))
    

    