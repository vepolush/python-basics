from random import random, randint


MIN = 0
MAX = 100
rand_int = randint(MIN, MAX + 1)

MSG_ENTER_DATA = f"Enter your number from {MIN} to {MAX}: "
MSG_USER_INPUT = "You have entered {number}"
MSG_USER_WON = "CORRECT"
MSG_USER_MISSED = "Missed"
MSG_WRONG_INPUT = "Only numbers"
MSG_BIGGER = f"{MSG_USER_MISSED}: Bigger"
MSG_LOWER = f"{MSG_USER_MISSED}: Lower"
MSG_TOO_BIG_INPUT = "Too big input"

while True:
    print("~" * 80)
    user_data = input(MSG_ENTER_DATA).strip().lstrip()
    print(MSG_USER_INPUT.format(number=user_data))

    if not user_data.isdigit():
        print(MSG_WRONG_INPUT)
        continue

    user_data = int(user_data)

    if user_data == rand_int:
        print(MSG_USER_WON)
        break

    if user_data > MAX:
        print(MSG_TOO_BIG_INPUT)
    elif user_data > rand_int:
        print(MSG_LOWER)
    else:
        print(MSG_BIGGER)