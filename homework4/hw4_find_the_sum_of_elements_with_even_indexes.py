user_numbers = [6]
result = 0

if user_numbers:
    for index, number in enumerate(user_numbers):
        if index % 2 == 0:
            result += number

    result *= user_numbers[-1]

print(result)
