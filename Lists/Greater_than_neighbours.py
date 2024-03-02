user_input = input()
num_list = [int(num) for num in user_input.split()]

count = 0

for i in range(1, len(num_list)-1):
    if num_list[i] > num_list[i - 1] and num_list[i] > num_list[i + 1]:
        count += 1

print(count)
