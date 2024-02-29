str = input()

first_index = str.find('f')

if first_index == -1:
    print(-2)
else:
    second_index = str.find('f', first_index + 1)
    if second_index == -1:
        print(-1)
    else:
        print(second_index)
