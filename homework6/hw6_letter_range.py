from string import ascii_letters

user_letters = input("Enter two letters separated by a hyphen: ").strip()

letter_start = user_letters[0]
letter_finish = user_letters[-1]

letter_start_index = ascii_letters.index(letter_start)
letter_finish_index = ascii_letters.index(letter_finish)

print(ascii_letters[letter_start_index:letter_finish_index + 1])
