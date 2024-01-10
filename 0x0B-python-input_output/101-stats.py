#!/usr/bin/python3
"""
101-stats.py - Read stdin line by line and compute metrics
"""

import sys


def print_stats(total_size, status_codes):
    """
    Prints the computed statistics.

    Args:
        total_size (int): Total file size.
        status_codes (dict): Dictionary containing status codes and their
        counts.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))


def parse_line(line, total_size, status_codes):
    """
    Parses a line and updates the total size and status codes.

    Args:
        line (str): Input line to be parsed.
        total_size (int): Current total file size.
        status_codes (dict): Dictionary containing status codes and their
        counts.

    Returns:
        tuple: Updated total size and status codes.
    """
    try:
        parts = line.split()
        size = int(parts[-1])
        status_code = parts[-2]
        total_size += size

        if status_code in status_codes:
            status_codes[status_code] += 1
        else:
            status_codes[status_code] = 1

    except (ValueError, IndexError):
        # Ignore lines that don't follow the expected format
        pass

    return total_size, status_codes


def main():
    """
    Main function to read lines from stdin, compute metrics, and print
    statistics.
    """
    total_size = 0
    status_codes = {}

    try:
        for i, line in enumerate(sys.stdin, 1):
            total_size, status_codes = parse_line(
                line, total_size, status_codes
            )

            if i % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
