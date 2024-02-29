str = input()

first_h_index = str.find('h')
last_h_index = str.rfind('h')

result_str = str[:first_h_index + 1] + str[first_h_index + 1:last_h_index][::-1] + str[last_h_index:]

print(result_str)
