user_number = input("Enter a number: ")

user_number_int = int(user_number)

count = 1

while user_number_int > 9:
    user_number_list = list(user_number)
    for number in user_number_list:
        count *= int(number)
    user_number_int = count
    user_number = str(user_number_int)
    count = 1

print(user_number)
