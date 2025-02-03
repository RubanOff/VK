
data = [11,7,1,2]
target = 9
def twoSum(data, target):
    hash_map = {}

    # Fill in dictionary
    for i in range(len(data)):
        hash_map[data[i]] = i 
    
    # Find array number of two number sum
    for i in range(len(data)):
        diff = target - data[i]
        if diff in hash_map:
            return [i, hash_map[diff]]
        
    return "Not exist"

# Тесты
with open("Семинар №4/test_TwoSum.txt") as file:
    for counter, i in enumerate(file):
        if counter % 2 == 0:
            data = list(map(int, i.split()))
        if counter % 2 == 1:
            target = list(map(int, i.split()))
            print(data, target, end = " <-----> ")
            target = target[0]
            print(twoSum(data, target))
