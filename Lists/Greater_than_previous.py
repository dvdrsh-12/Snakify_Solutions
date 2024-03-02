str = input()
str = str.split()
list = [int(num) for num in str]

for i in range(1, len(list)):
        if list[i] > list[i - 1]:
            print(list[i])
