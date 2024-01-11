#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    N = len(roman_string)
    i = N - 1
    output = 0
    while i >= 0:
        output += rom_dict[roman_string[i]]
        i = i - 1
    return (output)

