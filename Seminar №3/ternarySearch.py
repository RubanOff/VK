# Тернарный поиск

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
target = 10

left = 0
right = len(arr) - 1

def ternarySearch(array, left, right, target):
    
    if len(arr) == 0:
        return print("Введите коректный массив!")

    while left < right:
        m1 = left + (right - left) // 3
        m2 = right - (right - left) // 3

        if array[m1] == target:
            return m1
        if array[m2] == target:
            return m2
        
        if target < array[m1]:
            right = m1 - 1
        elif target > array[m2]:
            left = m2 + 1
        else:
            left = m1 + 1
            right = m2 - 1


    return False

print(ternarySearch(arr, left, right, target))

