#!/usr/bin/python3

"""
This module contains a function to determine if all the boxes can be opened.
"""

def can_unlock_all(boxes):
    """
    Determines if all the boxes can be opened.

    :param boxes: A list of lists. Each box may contain keys to other boxes.
    :return: True if all boxes can be opened, else False.
    """
    if not boxes or not boxes[0]:
        # If there are no boxes or the first box is empty, we cannot open any box
        return False

    n = len(boxes)
    # Initialize a set to keep track of the boxes that can be opened
    opened_boxes = {0}

    # Use a stack to perform depth-first search
    stack = [0]

    while stack:
        current_box = stack.pop()

        # Iterate through the keys in the current box
        for key in boxes[current_box]:
            # If the key corresponds to a valid box and that box hasn't been opened yet
            if 0 <= key < n and key not in opened_boxes:
                opened_boxes.add(key)
                stack.append(key)

    # Check if all boxes have been opened
    return len(opened_boxes) == n
