#!/usr/bin/python3
for number in range(10):
    for num in range(number + 1, 10):
        if number == 8 and num == 9:
            print("{:d}{:d}".format(number, num))
        else:
            print("{:d}{:d}, ".format(number, num), end='')
