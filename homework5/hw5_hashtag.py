import string


user_string = input("Enter a string: ")

user_string = user_string[:139]
string_by_char = list(user_string.title())

for index, char in enumerate(string_by_char):
    if char in string.punctuation:
        string_by_char.remove(char)

for char in string_by_char:
    if char == ' ':
        string_by_char.remove(char)

result = '#' + ''.join(string_by_char)

print(result)
