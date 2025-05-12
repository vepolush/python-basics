from pprint import pprint
from func_practice.utils import get_entities_data, get_users_in_state


users = get_users_in_state("Mississippi")
pprint(users)
