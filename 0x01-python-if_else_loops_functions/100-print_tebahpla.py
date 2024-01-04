#!/usr/bin/python3
toggle = True
for alph in range(ord('z'), ord('a')-1, -1):
    upper = alph -32
    if toggle:
        print(chr(alph), end="")
    else:
        print(chr(upper), end="")
    toggle = not toggle
