import sys
from stats import (
    get_book_text,
    get_word_count,
    get_character_count,
    sort_characters
)

def print_report(book_path, word_count, sorted_character_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in sorted_character_count:
        print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")

def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    character_count = get_character_count(book_text)
    sorted_character_count = sort_characters(character_count)
    print_report(book_path, word_count, sorted_character_count)

main()