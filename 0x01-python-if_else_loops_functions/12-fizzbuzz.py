#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 100):
        result = ''
        if i % 3 == 0:
            result = 'Fizz'
            print('{} '.format(result), end='')
        elif i % 5 == 0:
            result = 'Buzz'
            print('{} '.format(result), end='')
        elif i % 5 == 0 and i % 3 == 0:
            result = 'FizzBuzz'
            print('{} '.format(result), end='')
        else:
            print('{} '.format(i), end='')
