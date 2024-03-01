a = 0
b = 1
i = 1
n = int(input())

while b <= n:
    if b == n:
        print(i)
        break
    c = a + b
    a = b
    b = c
    i += 1
    
if b > n:
    print(-1)
