def get_unique_values(some_iterable: list | str | set) -> set:
    unique_values = set(some_iterable)
    return unique_values


# divide two numbers, get 0 if impossible
def get_division(dividend: int, divisor: int) -> int | float:
    """
    Returns 0 if divisor is 0 because of task #56565
    """
    if not divisor:
        return 0
    result = dividend / divisor
    return result


def send_email(recipient: str, email_body: str) -> None:
    print("sending email to {}...".format(recipient))


def send_email_to_manager() -> None:
    manager_email = 'example@ukr.net'
    text = "bla bla"
    send_email(manager_email, text)


def validate_not_hashable(value) -> None:
    hash(value)


def get_welcome_text() -> str:
    return "welcome"


def is_valid_email(email_candidate: str) -> bool:
    # if '@' in email_candidate:
    #     return True
    # return False
    result = '@' in email_candidate
    return result
