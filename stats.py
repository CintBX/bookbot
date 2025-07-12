def get_book_text(path):
    with open(path) as file:
        return file.read()

def get_word_count(text):
    return len(text.split())

def get_character_count(text):
    characters = {}
    for char in text:
        lowered = char.lower()
        if lowered in characters:
            characters[lowered] += 1
        else:
            characters[lowered] = 1
    return characters

def sort_on(items):
    return items["num"]

def sort_characters(characters):
    list_of_characters = []
    for key, val in characters.items():
        if key.isalpha():
            list_of_characters.append({ "char": key, "num": val })
    list_of_characters.sort(reverse=True, key=sort_on)
    return list_of_characters