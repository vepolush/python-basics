user_numbers = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

zeros = []
other_numbers = []


for number in user_numbers:
    if number == 0:
        zeros.append(number)
    else:
        other_numbers.append(number)

result = other_numbers + zeros

print(result)
