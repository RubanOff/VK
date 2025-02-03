
# Дан массив не отсортированных чисел.
# Необходимо найти максимально длинную возрастающую последовательность и вернуть ее длину


def FindLIS(array):

    if len(array) == 0:
        return 0
    if len(array) == 1:
        return 1
    
    dp = [1] * len(array)
    
    for i in range(1, len(array)):
        if array[i - 1] < array[i]:
            dp[i] = dp[i - 1] + 1

    return max(dp)


array = [8, 8, 8, 8] 
print(FindLIS(array))
