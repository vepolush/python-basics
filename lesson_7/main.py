from lesson_7.utilis import get_division, get_unique_values, validate_not_hashable, send_email_to_manager, \
    is_valid_email, send_email
from utilis import get_unique_values


my_unique_values1 = get_unique_values("some_iterable")
my_unique_values2 = get_unique_values([56])
my_unique_values3 = get_unique_values({5, 6})

validate_not_hashable(5)
send_email_to_manager()

email = 'example2@ukr.net'
if is_valid_email(email):
    send_email(email_body="hello", recipient=email)

fraction = get_division(10, 0)
print(fraction)
