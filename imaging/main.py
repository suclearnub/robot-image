import argparse
import numpy as np
import cv2
import preprocess.py as preprocess

ap=argparse.ArgumentParser()
ap.add_argument("-s", "--source", help="source of incoming images")
args = vars(ap.parse_args())

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
firstFrameSource = str.join('', (args["source"], "1.jpg"))
try:
    firstFrame = cv2.imread(firstFrameSource)
except Exception:
    print("File not found?")
    quit()

while True:
    cv2.imshow("First Frame", firstFrame)

    startX = grabIntInput("startX")
    endX = grabIntInput("endX")

    startY = grabIntInput("startY")
    endY = grabIntInput("endY")

    cv2.destroyAllWindows()

    #Y, X
    firstFrameCropped = firstFrame[startY:endY, startX:endX]
    cv2.imshow("Cropped Frame", firstFrameCropped)
    answer = input("Is this frame OK? [y/n] ")

    cv2.destroyAllWindows()

    if answer is "y" or "Y":
        break
    elif answer is "n" or "N":
        print("Please reselect.")
    else:
        print("Invalid input, assuming crop is OK.")
        break

while True:
    # TODO
    # Preprocess image

    # TODO
    # Find average "drift" from last frame

    # TODO
    # Send data to motors
    pass

