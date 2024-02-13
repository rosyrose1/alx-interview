#!/usr/bin/python3
'''LockBoxes Challenge'''


def canUnlockAll(boxes):
    '''Determines if all the boxes can be opened or not
    Returns:
        True: All boxes can be opened
        False: Not all boxes can be opened
    '''
    length = len(boxes)
    keys = set()
    opened_boxes = []
    r = 0

    while r < length:
        oldi = r
        opened_boxes.append(r)
        keys.update(boxes[r])
        for key in keys:
            if key != 0 and key < length and key not in opened_boxes:
                r = key
                break
        if oldi != r:
            continue
        else:
            break

    for r in range(length):
        if r not in opened_boxes and r != 0:
            return False
    return True
