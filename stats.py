import re
from collections import Counter
import stanza

nlp = stanza.Pipeline(lang='cs', 
                    logging_level='warning',
                    processors='tokenize,mwt,pos,lemma,depparse',
                    use_gpu=True)

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
    return re.sub(r'[^\w\s.§]', '', text)

def count_single_words(text: str) -> dict[str, int]:
    """Counts the number of single words in a text."""
    text = clean_text(text)
    return Counter(text.split())

def lemmatize_count_words(text: str, max_sentences=5) -> dict[str, int]:
    """Lemmatizuje a počítá slova po dávkách, aby se snížila spotřeba paměti."""
    
    text = clean_text(text)

    sentences = text.split(". ")  # Rozdělení na věty
    lemmatized_words = Counter()
    
    for i in range(0, len(sentences), max_sentences):
        batch_text = ". ".join(sentences[i:i+max_sentences])  # Vezmi max_sentences vět
        doc = nlp(batch_text)
        for sentence in doc.sentences:
            for word in sentence.words:
                lemmatized_words[word.lemma] += 1  

    return lemmatized_words
        