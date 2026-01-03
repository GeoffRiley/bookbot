#! /usr/bin/env python3
from pathlib import Path
from stats import get_num_words

BOOK_ROOT = Path("books")

def get_book_text(filepath: Path) -> str:
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book = "frankenstein.txt"
    text = get_book_text(BOOK_ROOT / book)
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")

main()


