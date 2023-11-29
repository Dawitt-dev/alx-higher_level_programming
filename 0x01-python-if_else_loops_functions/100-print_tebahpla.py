#!/usr/bin/python3
for ascii_value in range(ord('z'), ord('a') - 1, -1):
    if ascii_value % 2 == 0:
        char = chr(ascii_value) 
    else:
        char = chr(ascii_value - 32)
    print(char, end='')
