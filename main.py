import sys
from docx import Document

from stats import *


def get_book_text(path_to_file: str) -> str:
    """Reads the .txt file defined by ´path_to_file´ and returns the contents as a string"""
    
    if path_to_file.endswith(".docx"):
        doc = Document(path_to_file)
        book_text = ""
        for para in doc.paragraphs:
            book_text += para.text
        return book_text
    
    if path_to_file.endswith(".txt"):
        with open(path_to_file) as f:
            book_text = f.read()
        return book_text
    
    raise ValueError("File must be a .txt or .docx file")


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: python3 main.py [options] <path_to_book>")
        print(" --words, for word analysis")
        print(" --characters, for character analysis")
        print(" --lemmawords, for word lemmatized analysis")
        sys.exit(1)

    path_to_file = sys.argv[2]

    book_text = get_book_text(path_to_file)

    # Words analysis
    num_words = count_words(book_text)
    num_count = count_single_words(book_text)
    num_count_sorted = sort_by_value(num_count)

    if sys.argv[1] == "--lemmawords":
        lemmatized_count_words = lemmatize_count_words(book_text)
        lemmatized_count_words_sorted = sort_by_value(lemmatized_count_words)

    # Character analysis
    total_char_count = count_total_characters(book_text)
    char_count = count_signle_characters(book_text)
    char_count_sorted = sort_by_value(char_count)

    # Report printing
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")

    if sys.argv[1] == "--words":
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("----------- Single Word Counts >= 10 ----------")
        for word, count in num_count_sorted.items():
            if count < 10:
                continue
            print(f"{word}: {count}")

    if sys.argv[1] == "--lemmawords":
        print("----------- Lemmatized Single Word Count ----------")
        for word, count in lemmatized_count_words_sorted.items():
            if word == ".":
                continue
            if count < 10:
                continue
            print(f"{word}: {count}")

    if sys.argv[1] == "--characters":
        print("----------- Total Character Count ----------")
        print(f"Found {total_char_count} total characters")
        print("--------- Alphabetical Character Count -------")
        for char, count in char_count_sorted.items():
            if not char.isalpha():
                continue
            print(f"{char}: {count}")
    print("============= END ===============")


