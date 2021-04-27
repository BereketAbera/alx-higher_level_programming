#!/usr/bin/python3
def print_last_digit(number):
    number = (number * -1) if (number < 0) else number
    last_digit = number % 10
    print(last_digit, end='')
    return last_digit
