#!/usr/bin/python3
"""
0-stats.py
"""

import sys
import signal

total_size = 0
status_codes = {}
line_count = 0


def signal_handler(signal, frame):
    """
    Handles the SIGINT signal by printing the statistics and
    exiting the program.
    """
    print_statistics()
    sys.exit(0)


def print_statistics():
    """
    Prints the total size and the count of each status code.
    """
    print(f"File size: {total_size}")
    for status in sorted(status_codes.keys()):
        print(f"{status}: {status_codes[status]}")


signal.signal(signal.SIGINT, signal_handler)


def main():
    """
    Main function that reads from the standard input and parses the input.
    """
    global total_size, status_codes, line_count

    try:
        for line in sys.stdin:
            parts = line.split('"')
            if len(parts) == 3:
                ip, rest = parts[0].split(' - ')
                method, url, rest = parts[1].split(' ')
                status, size = parts[2].split()[-2:]

                if url == "/projects/260" and method == "GET":
                    try:
                        size = int(size)
                        total_size += size
                        status = int(status)
                        if status in [200, 301, 400, 401, 403, 404, 405, 500]:
                            status_codes[status] = status_codes.get(status, 0) + 1
                    except ValueError:
                        pass

            line_count += 1
            if line_count % 10 == 0:
                print_statistics()
    except KeyboardInterrupt:
        print_statistics()
        sys.exit(0)


if __name__ == "__main__":
    main()
