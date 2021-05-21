#!/usr/bin/python3
"""
    text_indentation
    print indentation after characters
    returns nothing
"""


def text_indentation(text):
    """
        prints indentation after characters
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    printed_line_chars = 0
    space_count = 0
    for c in text:
        if printed_line_chars == 0 and c == ' ':
            continue
        if c == ' ':
            space_count += 1
            continue

        if c not in ".?:":
            print(' ' * space_count, end='')
        space_count = 0
        print(c, end='')
        printed_line_chars += 1

        if c in ".?:":
            print("\n")
            printed_line_chars = 0
            space_count = 0
