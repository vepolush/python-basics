def correct_sentence(text: str) -> str:
    """
    Returns a correct copy of provided 'text' so that it always starts with a capital letter and ends with a period
    """
    if text[0].islower():
        text = text.replace(text[0], text[0].upper(), 1)

    if text[-1] != '.':
        text += '.'
    return text


assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')
