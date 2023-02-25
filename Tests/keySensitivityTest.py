from PIL import Image
import imagehash
from helperFunctions import *
from keyExchange import generateKeys
from imageEncoder import textToImage
from encrypt import encryptImage
from decrypt import decryptImage
from imageDecoder import imageToText
import numpy as np
from PIL import Image
from math import *
import csv
import time
#Calculates 1000 similarities by encrypting the text 1000 times, using the same key
differences=[]
for loop in range(100):
    startTime=time.time()
    bobPublicKey,BobSharedKey=generateKeys(100)
    print(loop)
    print("Generated keys")
    #Maybe I should actually generate the keys for this test

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

        
    im=Image.fromarray(array,mode="RGB")
    im.save("image.png")
    plaintextImagePixels=array#I do this because 
    imageFile="image.png"

    
    encryptedPixels,imageHash, nonce, encryptedImageFile=encryptImage(bobPublicKey,BobSharedKey,plaintextImagePixels,imageFile)

    im=Image.fromarray(plaintextImagePixels,mode="RGB")
    im.save("Image1.png")
    print("Encrypted")
    
    decryptedImagePixels,decryptedImageFile=decryptImage(imageHash,nonce,encryptedPixels,bobPublicKey,BobSharedKey-1)
    im=Image.fromarray(decryptedImagePixels,mode="RGB")

   
    im.save("Image2.png")
    hash1=imagehash.average_hash(Image.open('Image1.png'))
    hash2=imagehash.average_hash(Image.open('Image2.png'))
    print("Here")
    differences.append(hash1-hash2)
    endTime=time.time()
    print(endTime-startTime)
    
    
counter=1
with open("similarityKeySensitivity.csv","w") as f:
    writer = csv.writer(f)
    for value in enumerate(differences):
        writer.writerow((counter,value[1]))
        counter+=1
print(differences)
# 0