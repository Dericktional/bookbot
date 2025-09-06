def sort_on(chars):
    return chars["count"]

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

def sort_char_count(char_count):
    sorted_list = []

    for char in char_count:
        sorted_list.append({"char": char, "count": char_count[char]})

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list