from statsmodels.sandbox.stats.runs import runstest_1samp 
from tqdm import tqdm
import time
import hashlib
from matplotlib import pyplot as plt

'''
Parameter explanation:

x0 is the inital value of the x variable in the logistic map

r is the r value in the logistic map

i is the number of iterations used in the logistic map

sequenceSize is how many numbers are generated

returnVal is what index number is returned in the list of numbers generated, default is none, meaning it will return the last value

digits is how many digits the number generated should be, the default is 15

'''


def generateSequence(x0,r,i,sequenceSize,returnVal=None,digits=None):#The inital values, the index to return the random value, the number of random sequences to generate, and the optino to return the entire list. How many digitrs the numbers in the sequence should have
    if digits==0:
        digits=15
    def listToInt(array):#Converts a list into an integer
        final=""
        for a in array:
            final+=str(a)
        return int(final)

    def hexToInt(string):#Converts a hexadecimal number to an integer
        return int(string,16)

    def mix(integer,integer2):
        return integer^integer2
        

    def generate(x0,r,i):#Generates the logistic 
        linking={0:x0}
        for iteration in range(1,i+1):
            previousValue=float(linking[iteration-1])
            linking[iteration]="{0:.15}".format((r*previousValue)*(1-previousValue))
        valueList=list(linking.values())#A list of all the values within the current logisitic map
        final=str(valueList[-1])[2:]#Removes the decimal
        final=list(map(int,list(final)))#Formats it into a list of integers
        return final

    sequences=[]

    randomValues=[]#To hold all of the values generated
    initalValues=[(x0,r,i)]
    #Trying to find the period when the inital values will end up repeating?
    for a in (range(sequenceSize)):#Number of values to generate

        # start_time=time.time()
        sequence=generate(x0,r,i)
        if a==0:
            randomValues.append(listToInt(sequence))
        else:
            
            newValue=mix(int(randomValues[-1]),listToInt(sequence))

            newValueHash=hashlib.sha256(str(newValue).encode()).hexdigest()
            newValue=str(hexToInt(newValueHash))[0:15]
            
            if digits==None:#Limits the size
                randomValues.append(int(newValue))
            else:
                randomValues.append(int(newValue[0:digits]))
                
            sequence=newValue#Maybe I should keep this line? It might increase randomness
            #What this allows for is that, if the state of algorithm is revealed, the attacker won't be able to predict new sequences, as it relies on previous sequences, which are protected by a hash.
        #New idea. I take the hash of the sequence that is used to generate the keys. I turn the hash into the decimal. Then the new inital conditions are derived from there. If the attacker manages to rescontruct the dedcimal number and turn it back to hexcedimal, the attacker still doesn't know the previous number that was used, as the hash is a one way function.

        # if listToInt(sequence) in sequences:#Sequences also end getting repeated, my generation function just isn't that good.
        #     testing=sequences.index(listToInt(sequence))
        #     print(initalValues[testing])
        #     print("")
        #     print((x0,r,i))
        #     break#The issue here is that, although the inital value, and i are different, if r is the same, the the results are the same.
        #     #An example is (0.4971, 3.7742000000000036, 3871) and (0.1497, 3.7742000000000036, 7350)

        sequences.append(listToInt(sequence))
        
        newSequenceHash=hashlib.sha256(str(sequence).encode()).hexdigest()
        newSequence=str(hexToInt(newSequenceHash))[0:15]#Takes the current sequence's hash, then converts it into decimal to generate the new keys.This makes it so that attacker cannot backtrack to reveal future messages.

        x0=int(str(newSequence[0])+str(newSequence[4])+str(newSequence[8])+str(newSequence[12]))/10000#Creates a new x0 value

        # print(x0)

        r=int(str(newSequence[1])+str(newSequence[5])+str(newSequence[9])+str(newSequence[13]))/1000#I only do 1000 since, I want to have a new integer part as well. THe entire thing won't be decimal
        r+=3.5699#Making r fit withing the proper range for chaotic behaviour
        while r>4:
            r=r%4
            r+=3.5699
        # print(r)


        i=int(str(newSequence[2])+str(newSequence[6])+str(newSequence[10])+str(newSequence[14]))#Don't need to divide, because I want this to be in the thousands
        while i<1000:#Makin i fit within the proper range for chaotic behaviour
            i+=1000
        initalValues.append((x0,r,i))
        # if initalValues[-1] in initalValues:
        #     print(a)
        # print(f"{a} took {time.time()-start_time} seconds to run")
        # print(i)
        # print("")
        

    #What the current issue with my code is that, I end up getting repeated inital values, what that means is that the new random values only rely on different previous values. This is a problem, becuase over the long run, it won't be random.

    # print(runstest_1samp(randomValues))
    # plt.scatter(range(10000),randomValues)
    # plt.show()
    if returnVal=="list":
        return randomValues
    elif returnVal==None:
        return randomValues[-1]
    else:
        return randomValues[returnVal]
#The inital values, the index to return the random value, the number of random sequences to generate, and the optino to return the entire list.
