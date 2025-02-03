# Найти ближайшее целый корень числа


def binarySearchSqrt(number):
    left = 0
    right = number

    if number < 0:
        return print("Введите положительное значение! ")


    while left <= right:
        middle = (left + right) // 2
        if middle**2 > number:
            right = middle - 1
            continue
        if middle**2 < number:
            left = middle + 1
            continue
            
        return middle
    
    return right

number = 99

print(binarySearchSqrt(number))


