# Задача с принтерами

# x - скорость первого принтера
# y - скорость второго принтера
# n - количество листов

n = 20
x = 1
y = 15

def copyTime(n, x, y):
    left = 0
    right = (n - 1) * max(x, y)

    while left + 1 < right:
        middle = (right + left) // 2

        # middle/x + middle/y - количество листов, которые 2 принтера смогут напечатать на данный момент

        if middle/x + middle/y < n - 1:
            left = middle
        else:
            right = middle

    return right + min(x, y)


print(copyTime(n, x, y))

