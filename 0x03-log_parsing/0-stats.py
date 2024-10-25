#!/usr/bin/python3
import sys
import signal

total_size = 0
status_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_stats():
    """Prints the accumulated metrics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_count.keys()):
        if status_count[code] > 0:
            print("{}: {}".format(code, status_count[code]))


def signal_handler(sig, frame):
    """Handles keyboard interruption to print stats."""
    print_stats()
    sys.exit(0)


# Register the signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        # Validate and parse input format
        if (
            len(parts) >= 7 and
            parts[5] == '"GET' and
            parts[6] == '/projects/260'
        ):
            try:
                # Extract the status code and file size
                status_code = int(parts[8])
                file_size = int(parts[9])

                # Update metrics
                total_size += file_size
                if status_code in status_count:
                    status_count[status_code] += 1
            except (ValueError, IndexError):
                # Skip line if parsing fails
                continue

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
