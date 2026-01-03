#! /usr/bin/env python3
import sys
from pathlib import Path
from stats import get_num_words, char_frequency, sort_dictionary

def get_book_text(filepath: Path) -> str:
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def print_report(book):
    text = get_book_text(book)
    num_words = get_num_words(text)
    freqs = char_frequency(text)
    char_count = sort_dictionary(freqs)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for r in char_count:
        ch = r["char"]
        fr = r["num"]
        if ch.isalpha():
            print(f"{ch}: {fr}")
    print("============= END ===============")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = Path(sys.argv[1])
    # book = "frankenstein.txt"
    # text = get_book_text(BOOK_ROOT / book)
    # num_words = get_num_words(text)
    # print(f"Found {num_words} total words")
    # freqs = char_frequency(text)
    # print(freqs)
    # tmp = sort_dictionary(freqs)
    # print(tmp)
    print_report(book)

main()


