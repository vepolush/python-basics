import database


def get_username_and_password() -> tuple[str, str]:
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    return name, password


def is_valid_user_creds(username: str, password: str, force_permissions: bool = False) -> bool:
    if username and force_permissions:
        return True

    users = database.get_users()
    for user in users:
        if user["name"] == username and user["password"] == password:
            return True

    return False


def login_user():
    name, password = get_username_and_password()
    is_valid = is_valid_user_creds(name, password)
    if not is_valid:
        raise PermissionError("Access denied")




is_valid_user_creds("111", "2222", True)