import string


user_string = input("Enter a string: ")

string_by_char = list(user_string.title())

for index, char in enumerate(string_by_char):
    if char in string.punctuation:
        string_by_char.remove(char)

for char in string_by_char:
    if char == ' ':
        string_by_char.remove(char)

string_by_char_join = ''.join(string_by_char)
string_by_char_join = string_by_char_join[:139]

result = '#' + string_by_char_join

print(result)
