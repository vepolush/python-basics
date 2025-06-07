user_data = ["Alex", "Trump", 25, "Marta", "Alexis"]


user_fullname_slice = slice(0, 2)
partner_fullname_slice = slice(3, None)

full_name = user_data[user_fullname_slice]
partner_full_name = user_data[partner_fullname_slice]
print(full_name)
print(partner_full_name)
