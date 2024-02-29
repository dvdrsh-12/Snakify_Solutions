str = input()
length = len(str)
middle = (length + 1) // 2

first_half = str[:middle]
second_half = str[middle:]

new_string = second_half + first_half

print(new_string)