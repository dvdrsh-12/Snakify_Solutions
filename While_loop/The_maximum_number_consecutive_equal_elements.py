max_length = 0
current_length = 1
previous_number = 0

while True:
    number = int(input())

    if number == 0:
        break
    
    if number == previous_number:
        current_length += 1
    else:
        current_length = 1

    if current_length > max_length:
        max_length = current_length

    previous_number = number

print(max_length)
