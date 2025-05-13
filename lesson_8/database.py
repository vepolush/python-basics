import os
import json
import constants


def setup_database() -> None:
    """
    Create database connection
    """
    database_name = constants.DATABASE_NAME
    if os.path.exists(database_name):
        return

    with open(database_name, mode='w', encoding="utf-8") as database_file:
        json.dump([], database_file)

    print("no")


def get_users() -> list[dict]:
    with open(constants.DATABASE_NAME, encoding="utf-8") as storage:
        return json.load(storage)