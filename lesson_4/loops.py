from pprint import pprint


# some_list = [55, 666] * 6
# some_string = "h1094i2noa"
# products = ["banana", "vodka", "iuu", "milk", "bread", "vodka"]
#
# for product in products:
#     if product == "milk":
#         break
#
#     if product == "vodka":
#         continue
#
#     print(product)
#     if product == "vodka":
#         print("No booze today")
#
# print(8888888)


# people = [
#     ["Alex", "Bush", "Odesa", 35, False, 10512],
#     ["Petr", "Kovalsky", "Odesa", 35, True, 18502],
#     ["Alex", "Bush", "Odesa", 65, False, 75015],
#     ["Olga", "Butterfly", "Kyiv", 22, True, 14444],
#     ["Vitaliy", "Bondarenko", "KYIV", 22, True, 14444],
#     ["Vladyslav", "Shulepov", "Kyiv", 16, False, 10925],
#     ["Bogdan", "Kurva", "kharkiv", 29, False, 10025],
# ]

# all_maried_people = []
# not_married_from_city = []
# city = "Kyiv"
# total_age = 0
######################################
# for person in people:
#     name, surname, address, age, is_married, inn = person

    # # is_married = person[4]
    # # address = person[2].lower()
    # address = address.lower()
    # if is_married:
    #     all_maried_people.append(person)
    # if not is_married and city.lower() in address.lower():
    #     not_married_from_city.append(person)

# if all_maried_people:
#     for married_person in all_maried_people:
#         age = married_person[3]
#         total_age += age
#     print(f"average age or married people = {total_age/len(all_maried_people)}")
# else:
#     print("No married people = no age")
#
#
#
#
# print("all married")
# pprint(all_maried_people)
# print(f"not maried frm {city}")
# pprint(not_married_from_city)
####################################

# average age of married people
# 3 Alex below 22






# all maried people
# all_maried_people = []
#
# for person in people:
#     is_married = person[4]
#     if is_married:
#         all_maried_people.append(person)
#
# pprint(all_maried_people)


# not married from chosen city
# not_married_from_city = []
# city = "Kyiv"
#
# for person in people:
#     is_married = person[4]
#     address = person[2].lower()
#     if not is_married and city.lower() in address:
#         not_married_from_city.append(person)
#
# pprint(not_married_from_city)


# WARNING
list_string = "123"



# WARNING
list_data = [55, 66]
for number in list_data:
    print(number)
    new_number = number * 2
    list_data.append(new_number)