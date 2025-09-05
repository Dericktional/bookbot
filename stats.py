def get_book_text(filepath):
    return filepath.read()

def get_num_words(book):
    return len(book.split())

def get_char_count(book):
    book_chars = list(book)
    char_count = {}

    for char in book_chars:
        if char.lower() in char_count:
            char_count[char.lower()] += 1
        else:
            char_count[char.lower()] = 1
    return char_count