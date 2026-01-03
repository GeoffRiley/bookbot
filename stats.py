#! /usr/bin/env python3
from collections import Counter

def get_num_words(text: str) -> int:
    return len(list(text.split()))

def char_frequency(text: str) -> dict[str, int]:
    counts = Counter(text.lower())
    return dict(counts)

def sort_dictionary(letter_list: dict[str, int])->list[dict[str,str|int]]:
    new_dict = [{"char": ch, "num": n} for ch, n in letter_list.items()]
    sorted_list = sorted(new_dict, reverse=True, key=lambda x: x["num"])
    return sorted_list

