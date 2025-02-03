# Интерполяционный поиск

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
target = 5

def interpolationSearch(array, target):

    if len(arr) == 0:
        return print("Введите коректный массив!")

    left = 0
    right = len(array) - 1

    # Выполняем поиск пока заданное число в пределах массива

    while array[left] < target and target < array[right]:
        if array[left] == array[right]:
            break

        index = left + (right - left) * (target - array[left]) // (array[right] - array[left])

        if array[index] > target:
            right = index - 1
        elif array[index] < target:
            left = index + 1
        else:
            return index
    
    if array[left] == target:
        return left
    if array[right] == target:
        return right
    
    return False

print("Индекс числа: " , interpolationSearch(arr, target))