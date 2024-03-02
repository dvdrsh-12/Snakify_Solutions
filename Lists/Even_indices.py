str = input()
str = str.split()
numbers = [int(num) for num in str]

for i in range(0,len(numbers),2):
    
    print(str[i])