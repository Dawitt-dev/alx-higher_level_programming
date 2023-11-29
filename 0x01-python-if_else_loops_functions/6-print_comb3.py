#!/usr/bin/python3
for number in range(10):
    for num in range(number +1, 10):
        print("{:d}{:d}".format(number, num), end=', ' if number < 9 or num < 8 else '\n')
