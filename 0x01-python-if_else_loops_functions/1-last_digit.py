#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
str = "Last digit of " + str(number) + " is " + str(last)
if last > 5:
    print(f"{str} and is greater than 5")
elif last == 0:
    print(f"{str} and is 0")
else:
    print(f"{str} and is less than 6 and not 0")