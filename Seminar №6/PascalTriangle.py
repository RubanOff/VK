# Треугольник Паскаля

def PascalTriangle(row, col):

    if col == 0 or col == row:
        return 1
    else:
        return PascalTriangle(row - 1, col - 1) + PascalTriangle(row - 1, col)

# Вывод масисва в консоль

n = 6
dp = []
for row in range(n):
    CurrentRow = []
    for col in range(row + 1):
        CurrentRow.append(PascalTriangle(row, col))

    dp.append(CurrentRow)

print(dp)