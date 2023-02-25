import random
def generateNumber(n):#Where n is the number of bits
    num=random.getrandbits(n)
    return num

def generateLowPrimes():
    numbers=[2]
    for a in range(3,400):
        if a%2!=0:#Makes sure number is not even, because that means it is not prime
            numbers.append(a)
    primes=[]
    counter=0
    while len(numbers)>0:
        start=numbers[counter]
        primes.append(start)
        for a in numbers:
            if a%start==0:
                numbers.remove(a)
    return primes

def millerRabin(num,rounds):
    temp=num-1
    s=0
    while temp%2==0:
        s+=1
        temp>>=1#The same as dividing by 2, BUT if it is a decimal, it truncates it, otherwise, it stays the same. It also doesn't turn the number into an exponent
    d=temp

    def testComposite(roundValue):#If the number is prime return False
        x=pow(roundValue,d,num)

        if x==1:
            return False#Is prime
        for a in range(s):
            if pow(roundValue, 2**a * d, num) == num-1:#This it the same as x**2 mod n, but without having to continously redefining the variable. 
                return False#Is prime
        return True#Is composite

    for c in range(rounds):
        roundValue=random.randrange(2,num-2)
        if testComposite(roundValue)==True:
            return False
    return True


lowPrimes=generateLowPrimes()
def lowPrimeCheck(n):
    while True:#Makes sure that the candidate random number is not divivisble by the first couple hundred primes
        counter=0
        candidate=generateNumber(n)
        for a in lowPrimes:
            if candidate%a==0:
                break
            else:
                counter+=1
        if counter==len(lowPrimes):
            break
    return candidate

def generateLargePrime(n):#Where n is th number of bits
    while True:
        candidate=lowPrimeCheck(n)#Generates a candidate that is not divisible by first couple hundred primes
        if millerRabin(candidate,20)==True:
            return candidate

# print(generateLargePrime(1024))
