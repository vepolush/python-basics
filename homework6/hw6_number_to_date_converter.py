user_number = int(input("Enter a number: "))

seconds_in_day = 24 * 60 * 60
seconds_in_hour = 60 * 60

num_days = user_number// seconds_in_day
num_hours = (user_number - (num_days * seconds_in_day)) // seconds_in_hour
num_minutes = (user_number - (num_days * seconds_in_day) - (num_hours * seconds_in_hour)) // 60
num_seconds = (user_number - (num_days * seconds_in_day) - (num_hours * seconds_in_hour) - (num_minutes * 60))

num_days = str(num_days)

if int(num_days) != 11 and num_days[-1] == '1':
    day_pronouns = "день"
elif (int(num_days) > 14 or int(num_days) <5) and num_days[-1] in ['2', '3', '4']:
    day_pronouns = "дні"
else:
    day_pronouns = "днів"

if num_hours < 10:
    num_hours = '0' + str(num_hours)
if num_minutes < 10:
    num_minutes = '0' + str(num_minutes)
if num_seconds < 10:
    num_seconds = '0' + str(num_seconds)

print(f"{num_days} {day_pronouns}, {num_hours}:{num_minutes}:{num_seconds}")
