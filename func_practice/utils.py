import requests
from constants import URL


def get_entities_data(entity_name: str) -> list[dict]:
    url = f'{URL}{entity_name}'
    params = {
        "limit": 50000
    }
    response = requests.get(url, params=params)
    response_json = response.json()
    entities = response_json[entity_name]
    return entities


def _get_user_contact_data(user: dict) -> dict:
    """Use only in get_users_in_state, created for size optimisation of an object"""
    sanitized_user_data = {
        "firstName": user["firstName"],
        "lastName": user["lastName"],
        "phone": user["phone"],
    }
    return sanitized_user_data


def get_users_in_state(state: str) -> list[dict]:
    users = get_entities_data("users")
    users_in_state = []
    for user in users:
        if user["address"]["state"] == state:
            user_contact = _get_user_contact_data(user)
            users_in_state.append(user_contact)
    users_in_state.append(users)
    return users_in_state
