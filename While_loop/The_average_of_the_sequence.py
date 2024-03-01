avg = 0
sum = 0
length = 0

while True:
    n = int(input())
    if n == 0:
        break
    sum = sum + n
    length = length + 1

print(sum / length)