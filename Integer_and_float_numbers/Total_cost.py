A = int(input())
B = int(input())
N = int(input())

total = (A * 100 + B) * N

dollars = total // 100
cents = total % 100

print("{} {:02d}".format(dollars, cents))
