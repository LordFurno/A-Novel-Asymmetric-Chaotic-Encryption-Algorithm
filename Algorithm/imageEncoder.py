from PIL import Image
import numpy as np
from math import *

import random#Place holder for my random generator

def textToImage(filename):
    def encodePixel(text):#Text is 3 charcters long
        return [ord(text[0]), ord(text[1]), ord(text[2])]




    with open(filename) as file:
        text=str(file.read())
        size=len(text)
        if size<48:
            size+=48-size
        size=ceil(sqrt(size/3))
        
        if 3*(size**2)>len(text):
            while 3*(size**2)>len(text):#Adds the random text values to complete the square
                
                randomValue=random.randint(65,122)#I'm just going to use the ranom module because my generator isn'tt built for limits like this
                while randomValue>=91 and randomValue<=97:
                    randomValue=random.randint(65,122)
                text+=chr(randomValue)
        else:#If it is equal, I still want to pad values because I need to have some randomness to protect against CPA attacks
            while 6*(size**2)>len(text):#Adds the random text values to complete the square   
                randomValue=random.randint(65,122)#I'm just going to use the ranom module because my generator isn'tt built for limits like this
                while randomValue>=91 and randomValue<=97:
                    randomValue=random.randint(65,122)
                text+=chr(randomValue)

        temp=0
        pixelValues=[]
        for chunks in range(int(len(text)/3)):
            chunk=text[temp:temp+3]
            pixelValues.append(encodePixel(chunk))
            temp+=3

        # print(size)
        #Might not need to have the code below
        if len(text)/3>len(pixelValues):#If there is left over pixels
            numOfLeft=len(text)-len(pixelValues)*3
            leftover=[]
            for a in range(numOfLeft,0,-1):
                leftover.append(ord(text[-1*a]))
            pixelValues.append(leftover)
            #Add the left over pixels to pixelValues list



        length=int(sqrt(len(pixelValues)))
        pixels=np.zeros((length,length,3),dtype="int8")#Maybe I should change to uint8
        counter=0
        for a in range(length):
            for b in range(length):
                pixels[a][b]=pixelValues[counter]#Pixel values
                counter+=1
        # pixels[0][0]=[0,0,0]
        im=Image.fromarray(pixels,mode="RGB")
        im.save("image.png")
    return (pixels,"image.png")
    
    

