user_input = input()
num_list = [int(num) for num in user_input.split()]

for i in range(0, len(num_list)-1, 2):
    temp = num_list[i]
    num_list[i] = num_list[i + 1]
    num_list[i + 1] = temp

for i in num_list:
    print(i,end=" ")
