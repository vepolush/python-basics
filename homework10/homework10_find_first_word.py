def first_word(text: str) -> str:
    """
    Returns first word of 'text'
    """
    text_punctuation = '.,'
    text_without_punctuation = text

    for char in text_without_punctuation:
        if char in text_punctuation:
            text_without_punctuation = text_without_punctuation.replace(char, ' ')

    text_without_punctuation = text_without_punctuation.strip()
    words_from_text = text_without_punctuation.split()
    first_word_from_the_text = words_from_text[0]

    return first_word_from_the_text


assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')
