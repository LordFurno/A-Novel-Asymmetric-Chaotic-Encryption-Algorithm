#This is where I have to compile all the programs together
from keyExchange import generateKeys
from imageEncoder import textToImage
from encrypt import encryptImage
from decrypt import decryptImage
from imageDecoder import imageToText
from helperFunctions import *
import numpy as np
from PIL import Image
from math import *
import time
import os

bobPublicKey,BobSharedKey=generateKeys(100)
print("Generated keys")
bobPublicKey=(362850226262860952683171340309, 85, 279967001721465557295804473049, 220978695315092983223537240144)
# BobSharedKey=238489905992510295214459819872#Do this, because it takes too long to run
imageOrText=str(input("Image[I] or Text[T]: "))
while imageOrText!="T" and imageOrText!="I":
    imageOrText=str(input("Enter either Image[I] or Text[T]: "))
    
if imageOrText=="T":
    #Text encryption
    print("File size:")
    print(os.stat("message.txt").st_size)
    plaintextImagePixels,imageFile=textToImage("message.txt")
    print("Encoded text to image")
    
elif imageOrText=="I":
    #Image encryption
    #I need to include a random element to the image encryption
    image = Image.open("inputImage.jpg")#This code can make it so I can encrypt an image, it allows me to test it easier
    width,height=image.size
    image.load()
    im = Image.new('RGB', image.size, (255, 255, 255))
    im.paste(image, None)#This is needed for some reason, honestly not sure why.


    array=np.asarray(im)

    squareLength=max(width,height)#The code down here pads the image with random pixels. This is to prevent CPA attacks with images
    if len(array)<squareLength:#If the image is in a landscape shape (width is larger than height) 
        while len(array)<squareLength:
            newRow=generatePixels(squareLength)
            array=np.append(array,[newRow],axis=0)
        paddedValues=squareLength-len(array)
        print("Pad number of rows") 
        
    elif len(array[0])<squareLength:#If image is in poster shape (Height is larger than width)
        newArray=np.zeros((squareLength,squareLength,3),dtype="uint8")
        for a in enumerate(array):
            tempArray=a[1]
            tempValues=generatePixels(squareLength-len(a[1]))
            for value in tempValues:
                tempArray=np.append(tempArray,[value],axis=0)
            newArray[a[0]]=tempArray
            
        paddedValues=squareLength-len(array[0])
        array=newArray
        print("Pad number of elements per row")
        
    else:#If image is perfect square
        squareLength+=1
        paddedValues=[]
        while len(array)<squareLength:
            newRow=generatePixels(squareLength-1)#I do this, so I pad the number of rows first, before padding number of elements per row
            array=np.append(array,[newRow],axis=0)
        paddedValues.append(squareLength-len(array))
        
        newArray=np.zeros((squareLength,squareLength,3),dtype="uint8")
        for a in enumerate(array):
            tempArray=a[1]
            tempValues=generatePixels(squareLength-len(a[1]))
            for value in tempValues:
                tempArray=np.append(tempArray,[value],axis=0)
            newArray[a[0]]=tempArray
            
        paddedValues.append(squareLength-len(array[0]))
        array=newArray
        print("perfect square")
        
    im=Image.fromarray(array,mode="RGB")
    im.save("image.png")
    print("File size:")
    print(os.stat("image.png").st_size)
    plaintextImagePixels=array#I do this because 
    imageFile="image.png"

    

start=time.time()
encryptedPixels,imageHash, nonce, encryptedImageFile=encryptImage(bobPublicKey,BobSharedKey,plaintextImagePixels,imageFile)
end=time.time()
print(end-start)
print("Encrypted image")
print(f"Image hash: {imageHash}")

# with open("encryptedMessage.txt","w") as f:
#     f.write(imageToText(encryptedPixels))
print(f"Length of encrypted text: {len(imageToText(encryptedPixels))}")


with open("message.txt") as f:
    text=str(f.read())
    size=len(text)
    
    


decryptedImagePixels,decryptedImageFile=decryptImage(imageHash,nonce,encryptedPixels,bobPublicKey,BobSharedKey)


if imageOrText=="T":#Remove padding for text
    numRandomValues=0#I need to remove the random padding the to the message
    if size<48:#Calculates how many values were padded
        numRandomValues=48-size
    else:
        size=ceil(sqrt(size/3))
        if 3*(size**2)>len(text):
            numRandomValues=3*(size**2)-len(text)
        else:
            numRandomValues=6*(size**2)-len(text)

    print(f"Number of random values that was padded: {numRandomValues}")

    decryptedText=imageToText(decryptedImagePixels)

    # print(decryptedText[0:len(decryptedText)-numRandomValues])#Removes padded values
    
else:#Remove padding for images
    #This just removes all padding
    newArray=np.zeros((height,width,3),dtype="uint8")#Create the array unpadded values will be fit into
    counter=0
    for row in enumerate(array):
        if counter<height:
            newArray[row[0]]=row[1][:width]
        counter+=1

    array=newArray
    im=Image.fromarray(array,mode="RGB")
    im.save("decryptedImage.png")
    print("Removed padding")
# print(imageToText(decryptedImagePixels))
print(np.array_equiv(plaintextImagePixels, decryptedImagePixels))

#Current issue right now is that, the replit is too slow to generate the chebyshev polynomials, to fix this I plan to, on my on computer pregenerate a ton of them and then simply call them from a text file on the replit.
