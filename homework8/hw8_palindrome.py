import string


def is_palindrome(text: str) -> bool:
    """
    Returns true if 'text' is palindrome, false overwise
    """
    text_without_punctuation = text

    for char in text:
        if char in string.punctuation or char == ' ':
            text_without_punctuation = text_without_punctuation.replace(char, '')

    text_without_punctuation_reversed = text_without_punctuation[::-1]

    if text_without_punctuation.lower() == text_without_punctuation_reversed.lower():
        return True
    return False


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
