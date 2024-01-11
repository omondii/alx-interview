#!/usr/bin.python3
""" canUnlockAll func that checks if boxes are all unlocked """
def canUnlockAll(boxes):
    """ Method to check if all boxes can be opened """
    for key in range(1, len(boxes)): #Loop to iterate over nos. from 1 to n - 1
        flag = False #Tracks if a key can open a box
        for box in range(len(boxes)):
            if key in boxes[box] and box != key:
                flag = True
                break
        if not flag:
            return False
    return True