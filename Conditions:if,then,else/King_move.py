col1 = int(input())
row1 = int(input())
col2 = int(input())
row2 = int(input())

if (col1 - col2) in [-1, 0, 1] and (row1 - row2) in [-1, 0, 1]:
    print("YES")
else:
    print("NO")