import math

n = int(input("Введите число: "))
count = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if math.cos(i ** 2 + n) > 0:
            count += 1
print(count)
print("Hello!")