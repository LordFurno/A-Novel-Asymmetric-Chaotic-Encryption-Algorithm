# from encrypt import hashAsInt, nonce, size, bobPublicKey, BobSharedKey
from PIL import Image
import numpy as np
import hashlib
from generator import generateSequence
import collections

def decryptImage(imageHash,nonce,encryptedPixels,publicKey,sharedKey):
    size=len(encryptedPixels)
    def hexToInt(string):#Converts a hexadecimal number to an integer
        return int(string,16)
    def limit(r,i,d=None):
        r+=3.5699#Making r fit withing the proper range for chaotic behaviour
        while r>4:
            r=r%4
            r+=3.5699
        while i<1000:#Makin i fit within the proper range for chaotic behaviour
            i+=1000
        if d!=None:
            while d>15:
                d-=10
            return (r,i,d)    
        else:
            return (r,i)
    
    def generateSeeds(string):#Derives the seeds from a string, returns a tuple
        length=len(string)
        i1=int(string[0:4])
    
        r1=int(string[4:10])/100000
    
        sequenceLength=size

        x1=int(string[10:length-2])
        x1=x1/10**(len(str(x1)))#This makes it a decimal
    
        d1=int(string[len(string)-2:])
    

        r1,i1,d1=limit(r1,i1,d1)#r,i,d
        if d1==0:
            d1=15
        return (x1,r1,i1,sequenceLength,d1)


    # bobPublicKey=(362850226262860952683171340309, 85, 279967001721465557295804473049, 220978695315092983223537240144)
    # BobSharedKey=238489905992510295214459819872#DO this because it takes too long

    #All of this is the exact same process as in the encryption file. The differences happen when I try to change the values back.

    imageFile="encryptedImage.png"
    encryptedPixels=np.asarray(Image.open(imageFile))#Gets the encrypted pixels

    m=sharedKey#Generates the m value in the same way as encrypting it.
    m=m^publicKey[0]
    m=m^publicKey[1]
    m=m^publicKey[2]
    m=m^publicKey[3]
    m=m^int(str(imageHash)[0:len(str(m))])#I do this so that the output doesn't match the hash so closely
    m=m^nonce
    tempHash=hashlib.sha256(str(m).encode()).hexdigest()
    m=hexToInt(str(tempHash))

    length=len(str(m))/4
    if length.is_integer:
        length=int(len(str(m))/4)+1
        
    seeds1=str(m)[0:length]
    seeds2=str(m)[length:length*2]
    seeds3=str(m)[length*2:length*3]
    seeds4=str(m)[length*3:]

    a=generateSeeds(seeds1)
    b=generateSeeds(seeds2)
    c=generateSeeds(seeds3)
    d=generateSeeds(seeds4)


    A=generateSequence(a[0],a[1],a[2],a[3],"list",a[4])#Used to create new pixels

    B=generateSequence(b[0],b[1],b[2],b[3],"list",b[4])#Used to shuffle the rows

    C=generateSequence(c[0],c[1],c[2],c[3],"list",c[4])#Used to create new pixels

    D=generateSequence(d[0],d[1],d[2],d[3],"list",d[4])#Used to shuffle the columns



        
    decrypt=np.zeros((size,size,3),dtype="uint8")

    for i in range(size):#Shifts the values of the pixels
        newRow=[]
        for k in range(3):
            row=list(zip(*encryptedPixels[i]))[k]
            row=list(row)#This is to turn the tuple into a list

        
            row=collections.deque(row)#Turns the row in a dqeque object so I can easily rotate it
            rotateValue=(A[i]+C[k])%size#Calculates how much I should rotate it
            row.rotate(rotateValue)#rotates it. Rotates to the right
            row=list(row)#Converts it to an np array
            newRow.append(row)#Adds the shifted values of the tuple into newrow.
        newRow=list(zip(newRow[0],newRow[1],newRow[2]))#Combines all the newly shifted values in to 3 length tuples which represent the pixel value
        for a in enumerate(newRow):
            decrypt[i][a[0]]=a[1]#Assigns the pixels into the new decrypted image.

        
            
    for a in range(size):#Shuffles the columns
        tempColumn=decrypt[:,a]#Gets the column of the image
        tempColumn=collections.deque(tempColumn)
    
        rotateValue=A[a]%size#Calculates the shift value

        tempColumn.rotate(rotateValue)#Cycles the column the right
    
        tempColumn=list(map(list,tempColumn))
    
        decrypt[:,a]=tempColumn
            
            
    for a in range(size):#Shuffles all the rows.
        tempRow=decrypt[a]
        tempRow=collections.deque(tempRow)
    
        rotateValue=D[a] % size#Calculates the shift value
    
        tempRow.rotate(rotateValue)#Cycles the rows to eht right

        tempRow=list(map(list,tempRow))#Formats the list properly
        decrypt[a]=tempRow

        
    decryptedImage=np.zeros((size,size,3),dtype="uint8")
    for i in range(size):#Changes the values
        for j in range(size):
            for k in range(3):
                seqeunceCalculation=(A[i]^B[j]^D[k])%256
                calculatedValue=abs(decrypt[i,j,k]^seqeunceCalculation)
                decryptedImage[i,j,k]=calculatedValue

    im=Image.fromarray(decryptedImage,mode="RGB")
    im.save("decryptedImage.png")
    return (decryptedImage,"decryptedImage.png")