# Удаление рядом стоящих дубликатов пфффф

def deleteDuplicate(str):

    stack = []
    for char in str:
        stack.append(char)
        if len(stack) > 1 and stack[len(stack) - 1] == stack[len(stack) -2 ]:
            stack.pop()
            stack.pop()
        
    return stack
    

str = 'cdffd'
print(deleteDuplicate(str))

str1 = 'uioouiouuo'
print(deleteDuplicate(str1))



