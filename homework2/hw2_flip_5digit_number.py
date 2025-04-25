user_number = int(input("Enter a 5-digit number: "))
reversed_num = 0

digit = user_number % 10
reversed_num = reversed_num * 10 + digit
user_number //= 10

digit = user_number % 10
reversed_num = reversed_num * 10 + digit
user_number //= 10

digit = user_number % 10
reversed_num = reversed_num * 10 + digit
user_number //= 10

digit = user_number % 10
reversed_num = reversed_num * 10 + digit
user_number //= 10

digit = user_number % 10
reversed_num = reversed_num * 10 + digit
user_number //= 10

print(reversed_num)
