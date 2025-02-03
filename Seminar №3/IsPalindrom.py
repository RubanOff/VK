# Является ли слово палиндромом
# Метод двух указателей

str = 'madam'

def isPalindrom(str):
    left = 0
    right = len(str) - 1

    while left < right:
        if str[left] != str[right]:
            return False
        if str[left] == ' ':
            left += 1 
            continue
        if str[right] == ' ':
            right -= 1
            continue
        left += 1
        right -= 1
    return True


print(isPalindrom(str))
