from random import randint


random_list = []
random_list_limits = randint(3, 10)

for i in range(random_list_limits):
    random_number = randint(1, 9)
    random_list.append(random_number)

new_list = [random_list[0], random_list[2], random_list[-2]]

print(f"A list of random numbers with random number of elements: {random_list}")
print(f"New list from 3 elements of the original list: {new_list}")
