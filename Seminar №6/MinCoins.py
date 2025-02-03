# Дан массив целых чисел coin, где каждое число - номинал монеты и некоторое число amount - сумма монет из массива. 
# Необходимо найти наименьшее количество монет, которое в сумме дало бы amount. Если такой комбинации нет - возвращаем -1
# coins = [1,2,5], amount = 11 Результат: 3
# Решение: 11 = 5 + 5 + 1

def MinCoins(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for j in coins:
            if i - j >= 0:
                dp[i] = min(dp[i], dp[i - j] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

# Пример использования
coins = [1, 2, 5]
amount = 11
result = MinCoins(coins, amount)
print(result)


