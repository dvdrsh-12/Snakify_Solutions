str = input()
str = str.split()
list=[int(num) for num in str]

for i in list:
    if i % 2 == 0:
        print(i)