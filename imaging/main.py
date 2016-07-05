import numpy as np
import cv2
import preprocess.py as preprocess

def isNumber(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

def grabIntInput(name):
    while True:
        print(name,"?")
        ret = input(">")
        if isNumber(ret):
            break
        else:
            print("Not a number.")
    return ret


# Let us assume that the first file is 1.jpg
firstFrame = cv2.imread("1.jpg")
cv2.imshow("First Frame", firstFrame)

startX = grabIntInput("startX")
endX = grabIntInput("endX")

startY = grabIntInput("startY")
endY = grabIntInput("endY")

cv2.destroyAllWindows()

#Y, X
firstFrameCropped = firstFrame[startY:endY, startX:endX]
cv2.imshow("Cropped Frame", firstFrameCropped)




# TODO
# Get first frame from camera, and then ask user for frame.

while True:
    # TODO
    # Preprocess image

    # TODO
    # Find average "drift" from last frame

    # TODO
    # Send data to motors
    pass

