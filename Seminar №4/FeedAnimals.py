
# Feed animals
# Input values: animals - massive of animal needs, food - massive of food
# Output value: count - number of animals fed

def shell_sort(array):
    n = len(array)
    gap = len(array)//2
    while gap > 0 :
        for i in range(n):
            m_gap = i
            while m_gap >= gap and array[m_gap] < array[m_gap - gap]:
                array[m_gap] , array[m_gap - gap] = array[m_gap - gap], array[m_gap]
                m_gap -= gap

        gap = gap//2
    
    return array

def feed_animals(animals, food):
    # Corner-case
    if len(animals) == 0 or len(food) == 0:
        return print("Введите корректные данные!")
    
    # Sorted arrays
    animals_sort = shell_sort(animals)
    food_sort = shell_sort(food)

    # Number of animals fed
    count = 0

    # Comprasion
    for i in food:
        if i >= animals[count]:
            count += 1

        if count == len(animals):
            break

    return count 
        

# Тесты
with open("Семинар №4/test_FeedAnimals.txt") as file:
    for counter, i in enumerate(file):
        if counter % 2 == 0:
            arr1 = list(map(int, i.split()))
        if counter % 2 == 1:
            arr2 = list(map(int, i.split()))
            print(arr1, arr2, end = " <-----> ")
            print(feed_animals(arr1, arr2))