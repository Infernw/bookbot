import sys

from stats import get_num_words
from stats import get_characters_counts
from stats import sorted_char_counts

def get_book_text(book):
    filepath = f"books/{book}.txt"
    try:
        with open(filepath) as f:
            content = f.read()
            return content
    except FileNotFoundError:
        print(f"{book} is not in the database")
        sys.exit(1)
    
def print_report(num_words, count_list, book):
    print("============ BOOKBOT ============")
    print(f"Analyzing {book}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in count_list:
        print(f"{i['char']}: {i['num']}")
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <bookname>")
        sys.exit(1)
    
    book_name = sys.argv[1].capitalize()
    words = book_name.split()
    book = "".join(words)
    book = book.lower()
    

    text = get_book_text(book)
    num_words = get_num_words(text)
    characters_counts = get_characters_counts(text)
    count_list = sorted_char_counts(characters_counts)
    print_report(num_words, count_list, book_name)

main()