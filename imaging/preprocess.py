import numpy as np
import cv2

def imagePreprocess(imageName):
    gray = cv2.cvtColor(imageName, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21,21), 0)
    return gray
