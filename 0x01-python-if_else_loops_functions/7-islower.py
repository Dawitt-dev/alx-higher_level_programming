#!/usr/bin/python3
def islower(c):
    return ord('a') <= ord(c) <= ord('z') 
print("a is {}".format("lower" if islower("a") else "upper"))

