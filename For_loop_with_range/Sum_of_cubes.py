n = int(input())
sum = 0
a = 1

for i in range(n):
    sum = sum + a ** 3
    a = a + 1
    
print(sum)