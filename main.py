from stats import *

def main():
    with open("books/frankenstein.txt") as f:
        book = get_book_text(f)
        print(
            f"{get_num_words(book)} words found in the document\n"
            f"{get_char_count(book)}"
        )

main()