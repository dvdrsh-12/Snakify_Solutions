user_input = input()
num_list = [int(num) for num in user_input.split()]

unique_elements = []

for num in num_list:
    if num_list.count(num) == 1 and num not in unique_elements:
        unique_elements.append(num)

for i in unique_elements:
    print(i,end=" ")
