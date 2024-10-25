#!/usr/bin/python3
"""
This script reads lines from standard input and computes metrics based on the
log format provided. It tracks the total file size and counts occurrences of
specific HTTP status codes. Statistics are printed every 10 lines and on
keyboard interruption (CTRL + C).

Input Format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
If the format does not match, the line is skipped.

Output Format:
After every 10 lines and/or upon interruption:
    - Total file size: sum of all <file size> values processed
    - Number of lines by status code (200, 301, 400, 401, 403, 404, 405, 500)
"""

import sys
import signal

# Initialize counters
total_file_size = 0
status_code_counts = {
    200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
}
line_count = 0


def print_stats():
    """Print the current statistics."""
    print("File size:", total_file_size)
    for code in sorted(status_code_counts):
        if status_code_counts[code] > 0:
            print("{}: {}".format(code, status_code_counts[code]))


def process_line(line):
    """Process a single line of log data."""
    global total_file_size, line_count
    try:
        parts = line.split()
        if len(parts) < 7:
            return  # Skip lines with an incorrect format

        # Extract status code and file size
        status_code = int(parts[-2])
        file_size = int(parts[-1])

        # Update metrics
        total_file_size += file_size
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1
        line_count += 1

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

    except (ValueError, IndexError):
        pass  # Ignore lines with parsing errors


def signal_handler(sig, frame):
    """Handle keyboard interruption (CTRL + C)."""
    print_stats()
    sys.exit(0)


# Register signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

# Read from stdin line by line
for line in sys.stdin:
    process_line(line)
