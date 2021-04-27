#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
p_number = (number * -1) if (number < 0) else number
last_digit = p_number % 10
if last_digit > 5:
    print("Last digit of {} is {} and {}".format(number, last_digit,
          "is greater than 5"))
elif last_digit == 0:
    print("Last digit of {} is {} and {}".format(number, last_digit,
          "is zero"))
else:
    print("Last digit of {} is {} and {}".format(number, last_digit,
          "is less than 6 and not 0"))
