# Рекурсивный тернарный поиск

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
target = 10

left = 0
right = len(arr) - 1

def ternarySearch(array, left, right, target):

    if len(arr) == 0:
        return print("Введите коректный массив!")


    if right >= left:
        m1 = left + (right - left) // 3
        m2 = right - (right - left) // 3

        
        if array[m1] == target:
            return m1
        if array[m2] == target:
            return m2
        
        if target < array[m1]:
            return ternarySearch(array, left, m1 - 1, target)
        elif target > array[m2]:
            return ternarySearch(array, m2 + 1, right, target)
        else:
            return ternarySearch(array, m1 + 1, m2 - 1, target)

    
    return False

print(ternarySearch(arr, left, right, target))
