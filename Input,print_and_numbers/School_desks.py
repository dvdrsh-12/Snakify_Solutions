s1 = int(input())
s2 = int(input())
s3 = int(input())

if s1 % 2 != 0:
    s1 = s1 + 1
if s2 % 2 != 0:
    s2 = s2 + 1
if s3 % 2 != 0:
    s3 = s3+1

print((s1 + s2 + s3) // 2)    