#!/usr/bin/python3
"""
lockboxes alx-interview
"""


def canUnlockAll(boxes):
    """
    to determine if you can open the lockboxes
    """
    keys = [0]
    for key in keys:
        for boxKey in boxes[key]:
            if boxKey not in keys and boxKey < len(boxes):
                keys.append(boxKey)
    if len(keys) == len(boxes):
        return True
    return False
