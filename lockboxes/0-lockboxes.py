#!/usr/bin/python3

"""Check if all boxes can be unlocked."""


def canUnlockAll(boxes):
    """
     @param boxes - A list of boxes to check. Must be sorted by key
     @return True if all boxes can be unlocked
    """
    unlocked_boxes = [0]

    # If the unlocked boxes are not in box then add them to unlocked_boxes.
    while True:
        bool = False
        # Add unlocked boxes to unlocked_boxes.
        for i in unlocked_boxes:
            # Add unlocked boxes to unlocked_boxes.
            for key in boxes[i]:
                # Add a box to unlocked_boxes.
                if key not in unlocked_boxes:
                    bool = True
        # If true break the loop until the next call to this function is true.
        if not bool:
            break

    return len(unlocked_boxes) == len(boxes)
