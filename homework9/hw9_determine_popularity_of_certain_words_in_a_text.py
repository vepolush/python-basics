def popular_words (text: str, words: list | set | tuple | dict) -> dict:
    """
    Returns a dictionary with words and count of their use in the 'text'
    """
    words_count = dict()
    words_from_text = text.lower().split()

    for word in set(words):
        words_count[word] = words_from_text.count(word)

    return words_count


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
