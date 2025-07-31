from stats import get_num_words
from stats import get_characters_counts

def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
        return content
    
def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(text)
    characters_counts = get_characters_counts(text)
    print(f"{num_words} words found in the document")
    print(characters_counts)

main()