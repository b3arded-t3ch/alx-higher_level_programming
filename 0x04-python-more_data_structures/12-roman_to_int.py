#!/usr/bin/python3
def roman_to_int(roman_string):
    arabic_num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    roman_num = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']

    i = 12
    roman_numeral = ''
    while roman_string != 0:
        if arabic_num[i] <= roman_string:
            roman_numeral += roman[i]
            roman_string = roman_string - arabic_num[i]
        else:
            i = i -1
    return (roman_numeral)

