#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics.

It processes lines in the format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
If the format does not match, the line is skipped.

The script computes:
- Total file size: Sum of all <file size> values
- Number of occurrences of each valid status code:
200, 301, 400, 401, 403, 404, 405, 500

Statistics are printed after every 10 lines and upon a keyboard interruption
(CTRL + C).
"""

import sys
import re

# Initialize total file size and status codes dictionary
total_file_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

# Define regex pattern to validate format
log_pattern = re.compile(
    r'^\S+ - \[\S+ \S+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
)


def print_stats():
    """
    Prints the accumulated statistics of file size and status codes.
    Only status codes with a count greater than zero are displayed.
    """
    print("File size: {}".format(total_file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


try:
    for line in sys.stdin:
        match = log_pattern.match(line)
        if not match:
            continue

        # Extract status code and file size from matched groups
        status_code = int(match.group(1))
        file_size = int(match.group(2))

        # Update total file size and status code count if valid
        total_file_size += file_size
        if status_code in status_codes:
            status_codes[status_code] += 1

        line_count += 1

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise
finally:
    print_stats()
