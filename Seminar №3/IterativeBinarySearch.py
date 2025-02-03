# Итерационный бинарный поиск


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
target = 5
def binarySearch(array, target):
    left = 0
    right = len(array) - 1
    if len(arr) == 0:
        return print("Введите коректный массив!")


    # корнер кейсы
    if target < array[0] or target > array[right]:
        return False
    
    while left < right:
        middle = (left + right) // 2
        
        if array[middle] == target:
            return middle
        
        if array[middle] > target:
            right = middle - 1
        else:
            left = middle + 1

    return right


print(binarySearch(arr, target))


