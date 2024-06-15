import numpy as np
# Нужно сделать через два поинтера
# Заполняем массив
print("Введите массив: ")
# Можно ручками
# arr = np.array([int(i) for i in input().split()])
# Функция переворота массива
def reverseArray(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left = left + 1
        right = right - 1

    return arr

# Вывод ручками
# print(reverseArray(arr))

# Тесты 
with open("/Users/eugene/Desktop/VK education/Семинар №1/test_1.txt") as file:
    for cl in file:
        inpt = list(map(int, cl.split()))
        print(inpt, end='<----->')
        print(reverseArray(inpt))