maxnum = -1
count = -1

while True:
    n = int(input())
    if n == 0:
        break
    if n > maxnum:
        maxnum = n
        count = 1
    elif n == maxnum:
        count = count + 1
        
print(count)
    
    