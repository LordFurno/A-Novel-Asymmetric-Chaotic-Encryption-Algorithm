# from imageEncoder import pixels,size
# from keyExchange import bobPublicKey,BobSharedKey
from generator import generateSequence
import hashlib
import collections
import numpy as np
from PIL import Image

#p is the first value in Bob's public key
#pk is the triplet of the rest of the values of Bob's public key
#x is the plaintext image

def encryptImage(publicKey,sharedKey,pixels,imageFileName):
    size=len(pixels)
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


    imageFile=imageFileName#Gets the hash of the image
    with open(imageFile,"rb") as f:
        bytes=f.read()
        imageHash=hashlib.sha256(bytes).hexdigest()
    hashAsInt=hexToInt(imageHash)


    # bobPublicKey=(362850226262860952683171340309, 85, 279967001721465557295804473049, 220978695315092983223537240144)
    # BobSharedKey=238489905992510295214459819872#DO this because it takes too long

    #I generate the nonce using the values of the public key. This should be secure as my prng also serves as a 1 way function
    rValue=str(publicKey[2])[4:9]
    iValue=str(publicKey[3])[3:7]
    rValue,iValue=limit(int(rValue),int(iValue),None)
    xValue=int(str(publicKey[3])[8:13])/100000
    nonce=generateSequence(xValue,rValue,iValue,100)    


    #The values I will be using for encryption are- Bob's public key, the shared key, the hash of the plain text message and a nonce as some of the parameters for the the i nital conditions for the generator function
    #The only issue is that, once I encrypt the image, I send it to the ALice to decrypt, but I also s3end the hash of the image and the nonce. So I have to make sure that how I create the values for the inital conditinos of the generator cannot be found
    # print(bobPublicKey)#Public
    # print(BobSharedKey)#Private
    # print(hashAsInt)#Public
    # print(nonce)#Public



    '''
    The current problem is that to create the sequences that I need to encrypt the image, I need a very long sequence of
    secret numbers, currently that is only the shaerd key. So what i need to do is use the other values to generate an even
    longer sequence of numbers that I can use to generate the random sequences for encryption. The way I apply the other values
    must be in a 1 way fucntion, as the comments above show that most of the values are public.
    '''

    #For now I think my method here is secure. I use the other values to create a longer sequence of numbers that should not
    #be able to be traced back. This means that with this I will create the inital seeds for my generator to encrypt the image.
    m=sharedKey
    m=m^publicKey[0]
    m=m^publicKey[1]
    m=m^publicKey[2]
    m=m^publicKey[3]
    m=m^int(str(hashAsInt)[0:len(str(m))])#I do this so that the output doesn't match the hash so closely
    m=m^nonce

    tempHash=hashlib.sha256(str(m).encode()).hexdigest()
    m=hexToInt(str(tempHash))
    # print(f"Combined values: {m}")


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


    #generateseeds function works, turns out I might not even need to have 4 different starting seed values, I just need 3


    #According to the paper I was reading, I just use a couple of the sequences, to shift around the rows and columns. Then I just change the pixel values. Should be simple enough.
    #I can easily shift the values, as I can collections.deque and it has a built in rotate function. It works with numpy arrays too.


    #dtype HAS to be uint8
    encryptedImage=np.zeros((size,size,3),dtype="uint8")


    for i in range(size):#Changes the values
        for j in range(size):
            for k in range(3):
                seqeunceCalculation=(A[i]^B[j]^D[k])%256
                calculatedValue=abs(pixels[i,j,k]^seqeunceCalculation)
                encryptedImage[i,j,k]=calculatedValue



    for a in range(size):#Shuffles all the rows.
        tempRow=encryptedImage[a]
        tempRow=collections.deque(tempRow)
    
        rotateValue=D[a] % size#Calculates the shift value
    
        tempRow.rotate(-1*rotateValue)#Shifts the list, I multiply by -1, because I shift to left.

        tempRow=list(map(list,tempRow))#Formats the list properly
        encryptedImage[a]=tempRow



    for a in range(size):#Shuffles the columns
        tempColumn=encryptedImage[:,a]#Gets the column of the image
        tempColumn=collections.deque(tempColumn)
    
        rotateValue=A[a]%size#Calculates the shift value

        tempColumn.rotate(-1*rotateValue)#Shuffles the list, I multiply by -1, because I shift to left.
    
        tempColumn=list(map(list,tempColumn))
    
        encryptedImage[:,a]=tempColumn


    for i in range(size):#Shifts the values of the pixels
        newRow=[]
        for k in range(3):
            row=list(zip(*encryptedImage[i]))[k]
            row=list(row)#This is to turn the tuple into a list

            row=collections.deque(row)#Turns the row in a dqeque object so I can easily rotate it
            rotateValue=(A[i]+C[k])%size#Calculates how much I should rotate it
            row.rotate(rotateValue*-1)#rotates it. I multiply by -1 because I needs to shift to the left
            row=list(row)#Converts it to an np array
            newRow.append(row)#Adds the shifted values of the tuple into newrow.
            
        newRow=list(zip(newRow[0],newRow[1],newRow[2]))#Combines all the newly shifted values in to 3 length tuples which represent the pixel value
        for a in enumerate(newRow):
            encryptedImage[i][a[0]]=a[1]#Assigns the pixels into the new encrypted image.


            

    im=Image.fromarray(encryptedImage,mode="RGB")
    im.save("encryptedImage.png")
    return (encryptedImage,hashAsInt,nonce,"encryptedImage.png")

#Need to return the image hash and the nonce, and of course the image.