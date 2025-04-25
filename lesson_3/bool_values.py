import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


some_string = "I live in Kyiv since 2005:)"

some_new = some_string.isdigit()
result1 = False

digits = "56565"
result2 = True

##############################################################

# multiplier = 2
#
# if digits.isdigit():
#     digits_int = int(digits)
#     mult_result = digits_int * multiplier
#     logging.info(f"{mult_result=}")
# else:
#     logging.warning(f"Not int-like string provided: {digits}")

###############################################################

# user_login_candidate = ""
#
# if user_login_candidate.isdigit():
#     print("Your login must contain not only numbers")
# elif not user_login_candidate.isascii():
#     print("Only latin")
# elif not user_login_candidate:
#     print("Empty value prohibited")
# else:
#     print("OK")
#
#
# truthy = bool(user_login_candidate)
# truth2 = bool(0)
# truth3 = bool(0.0)

######################################################

# purchase_sum = 2522
# discount_card = 2
# seller_good_mood = True

###########################################

# DISCOUNT_0_1000 = 0
# DISCOUNT_1000_2000 = 5.5
# DISCOUNT_2000_5000 = 10
# DISCOUNT_5000_UP = 30

# if purchase_sum < 1000:
#     discount = DISCOUNT_0_1000 + discount_card
# elif purchase_sum < 2000:
#     discount = DISCOUNT_1000_2000 + discount_card
# elif purchase_sum < 5000 and discount_card > 2 and seller_good_mood:
#     discount = DISCOUNT_2000_5000 + (discount_card * 5)
# elif purchase_sum < 5000:
#     discount = DISCOUNT_2000_5000
# else:
#     discount = DISCOUNT_5000_UP

# print(f"Your {discount=}")

##########################################################

# is_person_child = False
# is_person_renter = True
#
# ########################################################
#
# ride_discount = 0
# ticket_cost = 100
#
# if is_person_child or is_person_renter:
#     ride_discount = 25
#
# discount_summ = (ticket_cost * ride_discount / 100)
# total = ticket_cost - discount_summ
# print(total)

str1 = "jj"
str2 = "jj"

if str1 != str2:
    print(2367246)

# delete by index


pass