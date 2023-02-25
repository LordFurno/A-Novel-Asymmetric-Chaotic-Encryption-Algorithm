from generator import *
from numpy import unique
from math import *
import csv
import time
import os
def calculateEntropy(randomValues):#I use 256 for the basis as verything because it is just simpler, it means the max entropy value is 
    randomValues=list(map(lambda x:x%256,randomValues))#I mod by 256, to limit all the values to 256, as it is easier to calculate entropy, and know how it compares to the max entropy
    _,counts=unique(randomValues,return_counts=True)
    #Returns entropy,max entropy
    total=sum(counts)
    sums=[]
    for value in counts:
        freq=value/total
        sums.append(log2(freq)*freq)
    randomSampleEntropy=sum(sums)*-1
    maxEntropy=log2(len(counts))
    return (randomSampleEntropy,maxEntropy)
numSamples=[10000,20000,40000,60000,80000,100000,200000]
toWrite=[]

start=time.time()
for num in numSamples:
    randomValues=generateSequence(0.9734,3.9748,6736,num,"list")
    calculated=calculateEntropy(randomValues)
    toWrite.append((1,num,calculated[0],calculated[1]))
    print(num)
end=time.time()
os.system('cls')
print("Row 1 done")
print(end-start)
print("")

start=time.time()
for num in numSamples:
    randomValues=generateSequence(0.6942,3.6779,8459,num,"list")
    calculated=calculateEntropy(randomValues)
    toWrite.append((2,num,calculated[0],calculated[1]))
    print(num)
end=time.time()
os.system('cls')
print("Row 2 done")
print(end-start)
print("")
    
start=time.time()
for num in numSamples:
    randomValues=generateSequence(0.1674,3.7188,7348,num,"list")
    calculated=calculateEntropy(randomValues)
    toWrite.append((3,num,calculated[0],calculated[1]))
    print(num)
end=time.time()
os.system('cls')
print("Row 3 done")
print(end-start)
print("")
    
with open("PRNGEntropy.csv","w") as f:
    writer = csv.writer(f)
    for row in toWrite:
        writer.writerow(row)