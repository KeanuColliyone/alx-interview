#!/usr/bin/python3
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
