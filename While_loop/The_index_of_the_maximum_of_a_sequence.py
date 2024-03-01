maxnum = -1
index = 0
maxindex = 0

while True:
    n = int(input())
    if n == 0:
        break
    index = index + 1
    if n > maxnum:
        maxnum = n
        maxindex = index

print(maxindex)