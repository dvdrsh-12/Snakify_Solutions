str = input()

result_str = ''.join(char for i, char in enumerate(str) if i % 3 != 0)

print(result_str)



