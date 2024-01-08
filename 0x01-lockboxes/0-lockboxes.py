#!/usr/bin/pythn3
# 0-lockboxes.py

def canUnlockAll(boxes):
    """A method that determines if all the boxes can be opened

    Args:
        boxes (list of lists): Contains the boxes to be opened
    """
    unlocked_boxes = set([0])
    unused_keys = list(boxes[0])

    while unused_keys:
        key = unused_keys.pop()
        if key < len(boxes) and key not in unused_keys:
            unlocked_boxes.add()
            unused_keys.extend()

    return len(unused_keys) == len(boxes)
