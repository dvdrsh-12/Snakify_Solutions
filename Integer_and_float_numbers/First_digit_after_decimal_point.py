num = float(input())

frac = num - int(num)
frac = frac * 10 * 10
frac = frac // 10
frac = int(frac)

print(frac)