from PIL import Image
import numpy as np
from math import *

def imageToText(pixels):
    def decodePixel(num):
        return chr(num)
    
    
    finalText=""
    for row in pixels:
        for pixel in row:
            for value in pixel:
                finalText+=decodePixel(value)
    return finalText

