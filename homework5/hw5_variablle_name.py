import string
from keyword import kwlist as register_words


user_string = input("Enter a string: ")

capital_letters = 'ABCDEFGHIGKLMNOPQRSTUVWXYZ'
is_validation_needed = True

for capital_letter in capital_letters:
    if capital_letter in user_string:
        is_validation_needed = False
        break

if is_validation_needed is True:
    for punctuation in string.punctuation:
        if punctuation == '_':
            continue
        elif punctuation in user_string:
            is_validation_needed = False
            break

if is_validation_needed is True:
    if len(user_string) > 1 and len(user_string) == user_string.count('_'):
        is_validation_needed = False
    elif user_string[0].isdigit():
        is_validation_needed = False
    elif ' ' in user_string:
        is_validation_needed = False
    elif user_string in register_words:
        is_validation_needed = False

print(is_validation_needed)
