#!/usr/bin/python3
"""
Module for UTF-8 validation.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing bytes of data.

    Returns:
        bool: True if data is valid UTF-8 encoding, otherwise False.
    """
    # Number of bytes in the current UTF-8 character
    n_bytes = 0

    # Mask to check the most significant 5 bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        # Get only the least significant 8 bits
        byte = num & 0xFF

        if n_bytes == 0:
            # Count the number of leading 1's to determine the number of
            # bytes in the UTF-8 character
            mask = 1 << 7
            while mask & byte:
                n_bytes += 1
                mask = mask >> 1

            # For 1-byte characters, n_bytes should be 0
            if n_bytes == 0:
                continue

            # UTF-8 characters are between 1 and 4 bytes
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # Check that the byte starts with '10'
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrement the count of bytes to process
        n_bytes -= 1

    # If n_bytes is not 0, it means we have an incomplete UTF-8 character
    return n_bytes == 0
