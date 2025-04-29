l = [1, 2, 3, 4, 5]

len_l = len(l)
number_of_items_in_first_list = -(-len_l//2)

first_list = l[0:number_of_items_in_first_list]
second_list = l[number_of_items_in_first_list:]

big_list = [first_list, second_list]

print(big_list)
