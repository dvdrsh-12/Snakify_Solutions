user_input = input()
num_list = [int(num) for num in user_input.split()]
count = 1
value = num_list[0]

for i in range(1, len(num_list)):
    if num_list[i] != value:
        count += 1
        value = num_list[i]

print(count)
