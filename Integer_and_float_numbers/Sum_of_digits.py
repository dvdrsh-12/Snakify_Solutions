num = int(input())

digit = num % 10
num = num // 10
digit = digit + num % 10
num = num // 10
digit = digit + num

print(digit)