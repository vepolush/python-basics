import database
import auth
from lesson_8 import utils


def main():
    database.setup_database()

    auth.login_user()


if __name__ == "__main__":
    main()
