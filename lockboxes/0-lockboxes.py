#!/usr/bin/python3

"""Check if all boxes can be unlocked."""


def canUnlockAll(boxes):
    """
     @param boxes - A list of boxes to check. Must be sorted by key
     @return True if all boxes can be unlocked
    """
    unlocked_boxes = [0]

    while True:
        Check = False
        for i in unlocked_boxes:
            for key in boxes[i]:
                if key not in unlocked_boxes:
                    unlocked_boxes.append(key)
                    Check = True
        if not Check:
            break

    return len(unlocked_boxes) == len(boxes)
