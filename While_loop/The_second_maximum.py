maxnum = -1
secmax = -1

while True:
    n = int(input())
    if n == 0:
        break
    if n > maxnum:
        secmax=maxnum
        maxnum=n
    elif secmax<n and n<maxnum:
        secmax=n
        
print(secmax)