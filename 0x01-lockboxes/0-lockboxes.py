from collections import deque
#!/usr/bin/pythn3
# 0-lockboxes.py

def canUnlockAll(boxes):
    """A method that determines if all the boxes can be opened

    Args:
        boxes (list of lists): Contains the boxes to be opened
    """
    num_boxes = len(boxes)
    unlocked_boxes = [False] * num_boxes
    unlocked_boxes[0] = True
    unused_keys = deque(boxes[0])

    while unused_keys:
        key = unused_keys.popleft()
        if key < num_boxes and not unlocked_boxes[key]:
            unlocked_boxes[key] = True
            unused_keys.extend(boxes[key])

    return all(unlocked_boxes)
