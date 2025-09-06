import sys
from stats import *

def main():
    if len(sys.argv) != 1:
        with open(sys.argv[1]) as f:
            book = get_book_text(f)

            print(
                f"============ BOOKBOT ============\n"
                f"Analyzing book found at {sys.argv[1]}...\n"
                f"----------- Word Count ----------\n"
                f"Found {get_num_words(book)} total words\n"
                f"--------- Character Count -------\n"
            )

            for dict in sort_char_count(get_char_count(book)):
                if dict["char"].isalpha():
                    print(f"{dict["char"]}: {dict["count"]}")

    else:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
main()