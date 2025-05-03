import string
from keyword import kwlist as register_words


user_string = input("Enter a string: ")

capital_letters = 'ABCDEFGHIGKLMNOPQRSTUVWXYZ'
another_check = True

for register_word in register_words:
    if len(user_string) == len(register_word) and register_word in user_string:
        print(False)
        another_check = False
        break

for capital_letter in capital_letters:
    if capital_letter in user_string:
        print(False)
        another_check = False
        break

for punctuation in string.punctuation:
    if punctuation == '_':
        continue
    elif punctuation in user_string:
        print(False)
        another_check = False
        break

if another_check is True:
    if len(user_string) > 1 and len(user_string) == user_string.count('_'):
        print(False)
    elif user_string[0].isdigit():
        print(False)
    elif ' ' in user_string:
        print(False)
    else:
        print(True)
