#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("0")
    else:
        a = 0
        for i in range(1, len(sys.argv)):
            a += int(sys.argv[i])
        print("{}".format(a))
