# Является ли одно строка подпоследовательность другой
# Методом 2 указателей


def isSubsequence(str1, str2):

    ptr1 = 0
    ptr2 = len(str1) - 1

    while ptr1 < len(str1) and ptr2 < len(str2):
        if str1[ptr1] == str2[ptr2]:
            ptr1 += 1
        ptr2 += 1 
        if ptr1 == len(str1):
            return True
    return False

str1 = 'elo'
str2 = 'hello'

print(isSubsequence(str1, str2))



        


        
