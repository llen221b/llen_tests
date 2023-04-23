def first_word(text: str) -> str:
    all_words = text.split()
    first_word= all_words[0]
    return(first_word)

assert first_word("Hello world") == "Hello"
assert first_word("a word") == "a"
assert first_word("greeting from CheckiO Planet") == "greeting"
assert first_word("hi") == "hi"