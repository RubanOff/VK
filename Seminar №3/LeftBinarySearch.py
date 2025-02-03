# Левый бинарный поиск (поиск первого вхождения)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 12]
target = 10

def leftBinarySearch(array, target):

    if len(arr) == 0:
        return print("Введите коректный массив!")
    
    left = 0
    right = len(array) - 1
    # ищем, пока не останется 2 элемента
    while left + 1 < right:
        middle = (left + right) // 2
        if array[middle] < target:
            left = middle
        else:
            right = middle

    # Начаинаем проверку с левой границе
    if array[left] == target:
        return left
    if array[right] == target:
        return right
    
    return False

print(leftBinarySearch(arr, target))
        

