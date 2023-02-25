from numpy import unique
from PIL import Image
import numpy as np
from math import *
from helperFunctions import generatePixels
import matplotlib.pyplot as plt
def getHistogram(image):
    R=[]
    B=[]
    G=[]
    for row in image:
        for pixel in row:
            R.append(pixel[0])
            G.append(pixel[1])
            B.append(pixel[2])
    _,rCount=unique(R,return_counts=True)
    _,gCount=unique(G,return_counts=True)
    _,bCount=unique(B,return_counts=True)
    valueRange=[]
    for a in range(0,256):
        valueRange.append(a)
    plt.bar(valueRange,rCount,color="red")
    plt.title("Red values")
    plt.show()
    
    plt.bar(valueRange,gCount,color="green")
    plt.title("Green values")
    plt.show()
    
    plt.bar(valueRange,bCount,color="blue")
    plt.title("Blue values")
    plt.show()


cipherImage = Image.open("encryptedImage.png")
cipherImage=np.asarray(cipherImage)

inputImage=Image.open("image.png")
inputImage=np.asarray(inputImage)

getHistogram(inputImage)
getHistogram(cipherImage)