user_input = input()
num_list = [int(num) for num in user_input.split()]

max_value = num_list[0]
index = 0

for i in range(1, len(num_list)):
    if num_list[i] > max_value:
        max_value = num_list[i]
        index = i

print(max_value,index)

