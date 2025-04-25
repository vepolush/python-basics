user_number = int(input("Enter a 4-digit number: "))

first_char = user_number // 1000
second_char = (user_number-first_char*1000) // 100
third_char = (user_number -  first_char*1000 - second_char*100) // 10
fourth_char = user_number % (first_char*1000 + second_char*100 + third_char*10)

print(first_char)
print(second_char)
print(third_char)
print(fourth_char)
