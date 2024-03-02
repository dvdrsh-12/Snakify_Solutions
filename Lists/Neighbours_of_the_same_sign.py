str1 = input()
list = str1.split()
list = [int(num) for num in list]

result = []

for i in range(1, len(list)):
    if (list[i] > 0 and list[i - 1] > 0) or (list[i] < 0 and list[i - 1] < 0):
        result = [list[i - 1], list[i]]
        break

result_str = " ".join(map(str, result))
print(result_str)
