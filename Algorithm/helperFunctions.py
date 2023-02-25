import numpy as np
import random
def generatePixels(length):
    def createPixel():
        return np.asarray((random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)))
    array=[]
    for a in range(length):
        array.append(createPixel())
    array=np.asarray(array)
    array = array = array.astype('uint8')
    return array
