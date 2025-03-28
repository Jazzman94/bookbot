import re
from collections import Counter

def count_words(text: str) -> int:
    """Counts the number of words in a text."""
    return len(text.split())

def count_total_characters(text: str) -> int:
    """Counts the number of characters in a text."""
    return len(text)

def count_signle_characters(text: str) -> dict[str, int]:
    """Counts the number of single characters in a text."""
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_by_value(char_count: dict[str, int]) ->  dict[str, int]:
    """Sorts the dictionary by value."""
    sorted_items = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
    return dict(sorted_items)

def clean_text(text):
    """Removes all non-alphanumeric characters from a text except § symbol and converts string to lowercase."""
    text = text.lower()
    return re.sub(r'[^\w\s§]', '', text)

def count_single_words(text: str) -> dict[str, int]:
    """Counts the number of single words in a text."""
    text = clean_text(text)
    return Counter(text.split())
        