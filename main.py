#! /usr/bin/env python3

from pathlib import Path

BOOK_ROOT = Path("books")

def get_book_text(filepath: Path) -> str:
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def count_words(text: str) -> int:
    return len(list(text.split()))

def main():
    book = "frankenstein.txt"
    text = get_book_text(BOOK_ROOT / book)
    num_words = count_words(text)
    print(f"Found {num_words} total words")

main()


