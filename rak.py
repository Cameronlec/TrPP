n = int(input("Введите число: "))
sum = 0
for i in range(1, n + 1):
    multi = 1
    for j in range(i, 2 * i + 1):
        multi *= j
    sum += multi
print(sum)