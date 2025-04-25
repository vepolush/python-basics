# some_string = "I live in Kyiv since 2005"
# #
# # other_result = some_string.split("i")
# # other_result_visual = ["I", "live", "in", "Kyiv", "since", "2005"]
#
# empty_list = []
#
# if empty_list:
#     print("5555555")
#
# not_empty_list = ["4545", 5555, True, 4.4, [], empty_list]
# if not_empty_list:
#     print("22222222222")
#
# fifth_elem = not_empty_list[4]
# # big_elem = not_empty_list[40]
# fifth_letter = some_string[4]
#
# len_list = len(not_empty_list)
# len_list2 = len(empty_list)
# len_list3 = len(some_string)

purchase_plan = ["banana"]

# add 1 elem
purchase_plan.append("salt")
purchase_plan.append("salt")
purchase_plan.append("2")

# marge by another list
sister_plan = ["bread", "milk"]
purchase_plan.extend(sister_plan)
# purchase_plan.extend("56247326")

# purchase_plan.sort()
# purchase_plan.sort(key=len, reverse=True)

# delete item
purchase_plan.remove("salt")

if "nails" in purchase_plan:
    purchase_plan.remove("nails")

if "abc" in "abcde":
    print("16321")


# delete by index
purchase_plan.pop()
purchase_plan.pop(0)

pass
