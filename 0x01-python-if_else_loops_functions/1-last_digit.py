#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
last_digit = (last_digit - 10) if (number < 0 and
                                   last_digit != 0) else last_digit
if last_digit > 5:
    print("Last digit of {} is {} and {}".format(number, last_digit,
          "is greater than 5"))
elif last_digit == 0:
    print("Last digit of {} is {} and {}".format(number, last_digit,
          "is 0"))
else:
    print("Last digit of {} is {} and {}".format(number, last_digit,
          "is less than 6 and not 0"))
