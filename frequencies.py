"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    Converted_list = []
    frequencies = {}
    for elments in items:
        converted = str(elments)
        if converted not in frequencies:
            frequencies[converted] = 1
        else:
            frequencies[converted] += 1
    return frequencies