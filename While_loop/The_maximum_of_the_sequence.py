maxnum = -1

while True:
    n = int(input())
    if n == 0:
        break
    if n > maxnum:
        maxnum = n

print(maxnum)
