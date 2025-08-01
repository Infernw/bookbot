import sys

from stats import get_num_words
from stats import get_characters_counts
from stats import sorted_char_counts

def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
        return content
    
def print_report(num_words, count_list, filepath):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in count_list:
        print(f"{i['char']}: {i['num']}")
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    characters_counts = get_characters_counts(text)
    count_list = sorted_char_counts(characters_counts)
    print_report(num_words, count_list, filepath)

main()