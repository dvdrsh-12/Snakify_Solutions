num = int(input())

if num >= 2:
    i = 2
    while i <= num:
        if num % i == 0:
            print(i)
            break
        i = i + 1