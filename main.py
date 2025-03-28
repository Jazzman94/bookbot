import sys

from stats import count_words, count_signle_characters, sort_by_value


def get_book_text(path_to_file: str) -> str:
    """Reads the .txt file defined by ´path_to_file´ and returns the contents as a string"""
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1]

    book_text = get_book_text(path_to_file)
    num_words = count_words(book_text)
    char_count = count_signle_characters(book_text)
    char_count_sorted = sort_by_value(char_count)

    # Report printing
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char, count in char_count_sorted.items():
        if not char.isalpha():
            continue
        print(f"{char}: {count}")
    print("============= END ===============")


