#!/usr/bin/python3

def uppercase(str):
    result_str = ''
    for char in str:
        if 'a' <= char <= 'z':
            result_str += chr(ord(char) - ord('a') + ord('A'))
        else:
            result_str += char
    return result_str
