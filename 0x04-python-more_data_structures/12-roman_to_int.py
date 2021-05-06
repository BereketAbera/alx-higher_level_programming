#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_chars = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                   'D': 500, 'M': 1000}
    if not isinstance(roman_string, str):
        return 0
    val = 0
    for c in roman_string:
        if c not in roman_chars:
            return 0
        val += roman_chars[c]
    return val
