#!/usr/bin/python3
"""
Module to check if all boxes can be unlocked.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    :param boxes: List of lists containing keys.
    :return: True if all boxes can be opened, otherwise False.
    """
    if not boxes or not isinstance(boxes, list):
        return False

    unlocked = [False] * len(boxes)
    unlocked[0] = True  # The first box is always unlocked
    keys = boxes[0]  # Get the keys from the first box

    # Try to unlock all boxes
    for key in keys:
        if key < len(boxes):
            unlocked[key] = True

    for i in range(len(boxes)):
        if unlocked[i]:
            for key in boxes[i]:
                if key < len(boxes):
                    unlocked[key] = True

    # Check if all boxes are unlocked
    return all(unlocked)
