print("Hello! Welcome to 'The simplest calculator!'")

first_num = float(input("Enter first number: "))
second_num = float(input("Enter second number: "))
math_operation = input("Enter an operation, you want to do with these numbers (+, -, *, /): ").strip()

if math_operation == '+':
    result = first_num + second_num
    print(f"{first_num} + {second_num} = {result}")
elif math_operation == '-':
    result = first_num - second_num
    print(f"{first_num} - {second_num} = {result}")
elif math_operation == '*':
    result = first_num * second_num
    print(f"{first_num} * {second_num} = {result}")
elif math_operation == '/' and second_num == 0:
    print("Zero division error. We cannot divide by 0")
elif math_operation == '/':
    result = first_num / second_num
    print(f"{first_num} / {second_num} = {result}")
else:
    print(f"{math_operation} is not a math symbol for operation!")
