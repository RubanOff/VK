# Дан массив целых чисел. Каждое число - стоимость акции. Нам нужно купить максимально дешево, 
# а продать максимально дорого. Сделать это надо за O(n)
# [8, 9, 3, 7, 4, 16, 12] - максимальная выгода 13. Купили за 3, продали за 16

def MaxProfit(prices):
    profit = 0
    min_price = prices[0]

    for i in range(len(prices)):
        profit = max(profit, prices[i] - min_price)
        min_price = min(prices[i], min_price)

    return profit


prices = [8, 9, 3, 7, 4, 16, 12]
print(MaxProfit(prices))