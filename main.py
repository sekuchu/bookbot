import sys
from stats import get_num_words
from stats import counter
from stats import sorter

def main():
    if(len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = get_book_text(sys.argv[1])
    number_of_words = get_num_words(book)
    dictionary = counter(book)
    list = sorter(dictionary)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")

    for combined_dict in list:
        print(f"{combined_dict["char"]}: {combined_dict["num"]}")
    print("============= END ===============")

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
main()