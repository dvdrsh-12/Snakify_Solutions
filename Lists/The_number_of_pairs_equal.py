user_input = input()
num_list = [int(num) for num in user_input.split()]

pair_count = 0

for i in range(len(num_list)):
    for j in range(i + 1, len(num_list)):
        if num_list[i] == num_list[j]:
            pair_count += 1

print(pair_count)
