# Линейный поиск 

arr = [1, 2, 3, 4, 5, 6]
elem = 4

def lineSearch(array, element):

    if len(arr) == 0:
        return print("Введите коректный массив!")
    
    lenght = len(array) - 1
    for i in range(lenght):
        if array[i] == element:
            return i

print(lineSearch(arr, elem))

