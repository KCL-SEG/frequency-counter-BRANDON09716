"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""
from collections import Counter
def frequencies(items):
    Converted_list = []
    frequencies = {}
    for elments in items:
        converted = str(elments)
        Converted_list.append(converted)
        counter = Counter(Converted_list)
    print(counter)
    return frequencies
