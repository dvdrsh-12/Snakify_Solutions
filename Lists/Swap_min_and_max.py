user_input = input()
num_list = [int(num) for num in user_input.split()]

max_value = max(num_list)
min_value = min(num_list)

max_index = 0
min_index = 0

for i in range(len(num_list)):
    if num_list[i] == max_value:
        max_index = i
    elif num_list[i] == min_value:
        min_index = i

num_list[min_index], num_list[max_index] = num_list[max_index], num_list[min_index]

for i in num_list:
    print(i,end=" ")
