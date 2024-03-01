a = 0
b = 1
i = 1
n = int(input())

while i <= n:
    c = a + b
    a = b
    b = c
    i = i + 1
    
print(a)