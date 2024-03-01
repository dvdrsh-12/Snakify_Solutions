count = -1
maxnum = 0

while True:
    n = int(input())
    if n == 0:
        break
    if n > maxnum:
        count = count + 1
    maxnum = n
    
print(count)
    