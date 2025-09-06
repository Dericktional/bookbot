import sys
from stats import *

def main():
    with open("books/frankenstein.txt") as f:
        book = get_book_text(f)

        print(
            f"============ BOOKBOT ============\n"
            f"Analyzing book found at books/frankenstein.txt...\n"
            f"----------- Word Count ----------\n"
            f"Found {get_num_words(book)} total words\n"
            f"--------- Character Count -------\n"
        )

        for dict in sort_char_count(get_char_count(book)):
            if dict["char"].isalpha():
                print(f"{dict["char"]}: {dict["count"]}")

main()