# Циклический сдвиг массива 
# k - колличество сдвигаемых элементов

# Массив ручками
#arr = list(map(int, input("Введите массив через пробел: ").split()))

k = input()

# Функция разворота массива(использовалась в 1C)
def reverseArray(arr, left, right):
        
    
    while(left < right):
        arr[left], arr[right] = arr[right], arr[left]
        left = left + 1
        right = right - 1
    
    return arr

def solution(arr, k):

    if len(arr) == 0:
        print("Введите непустой массив!")
        exit()
    else:
        n = len(arr)
        # Переворачиваем весь массив
        reverseArray(arr, 0, n - 1)
        # Переворачиваем первые k чисел
        reverseArray(arr, 0, (k % n) - 1)
        # Переворачиваем оставшийся массив
        reverseArray(arr, (k % n), n - 1)

        return arr

# Вывод массива ручками
#print(solution(arr, 3))


# Тесты 
with open("/Users/eugene/Desktop/VK education/Семинар №1/test_1.txt") as file:
    for i in file:
        inpt = list(map(int, i.split()))
        print(inpt, end = "<----->")
        print(solution(inpt, 3))
