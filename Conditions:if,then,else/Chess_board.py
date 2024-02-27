col1 = int(input())
row1 = int(input())
col2 = int(input())
row2 = int(input())

if (col1 + row1) % 2 == (col2 + row2) % 2:
    print("YES")
else:
    print("NO")