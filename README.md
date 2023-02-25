# Chaotic-encryption
A Novel Asymmetric Chaotic Encryption Algorithm











Table of Contents:

Abstract                                                                                              
Introduction                                                                                     
Background information                                                            
Design                     								     
Design criteria                                                                               
The proposed algorithm                                                                           
Testing and testing results                                                       
Security analysis                                                                          
Conclusion & application                                                         
Next steps
Bibliography
Appendix



I. Abstract

This paper proposes a novel chaos-based encryption algorithm for both images and text, addressing the increased need for secure and reliable encryption in today's digital age.  Although various chaos-based encryption algorithms exist and demonstrate the potential of chaos-based encryption, an asymmetric chaos-based encryption algorithm that encrypts both text and images is currently lacking. 
Previous research has demonstrated that chaos can be successfully used for encryption [1], however, a key part of the entire encryption process, the pseudorandom number generator, was often overlooked. For an encryption algorithm to be secure, the pseudorandom number generator used must be cryptographically secure. 
This encryption algorithm uses a Diffie Hellman key agreement protocol using the Chebyshev Polynomials [1,7].  This key agreement allows for the creation of 4 pseudorandom sequences which are then used to encrypt the input. If the input is text, I use a process originally used to compress files, to turn the text into an image. Afterwards, using the pseudorandom sequences, it changes, shifts, and shuffles rows and columns of the image pixels to get a new encrypted image. From here, the process can easily be reversed and decrypted. 
This algorithm proves resistant to chosen plaintext attacks, also known as CPA attacks, as the entire encryption process is randomized. 
The testing results demonstrate the fact that this algorithm is resistant to CPA attacks, performs better than other encryption algorithms of its kind and is overall quite secure. 




II. Introduction

With the increased traffic and use of the internet, the need for secure, fast and generally good encryption is needed more than ever. Current encryption algorithms include RSA, AES and many others. However, with the development of encryption algorithms, counters and workarounds to these encryptions continue to advance. Chaotic encryption is a promising concept that uses mathematical chaos to encrypt and decrypt media. Although there are chaotic encryption algorithms, they typically use a symmetric key exchange and only encrypt images. As a result, the encryption algorithm is used far less frequently. There is still a lack of a proper asymmetric chaotic encryption algorithm that encrypts text and images.
Another key aspect of chaotic encryption algorithms that is often overlooked is the pseudo-random number generators (PRNG) that act as the foundation for the rest of the algorithm. In many studies, the PRNG described is not cryptographically secure [1]. As a result, if the state of the PRNG is compromised, all future communications are threatened. This poses quite a security risk for if an attacker ever reveals the current state of the PRNG in use, the entire communication process between the parties is jeopardized. 
This algorithm uses a novel cryptographically secure PRNG, which is used to encrypt the media in a stream cipher-like fashion. What this means is that if the state of the PRNG is ever revealed to the attacker, all future communications remain secure. This algorithm also uses a Diffie-hellman key exchange as the key generator, making this encryption algorithm asymmetric. Additionally, the method this algorithm uses to encrypt media allows it to encrypt both text and images. 
Further details of the algorithm are described in section VI. 



III. Background information
	
	Chaos theory is the study of seemingly random or unpredictable behaviour that is governed by deterministic laws. Fundamentally, chaos theory is the sensitivity to initial conditions, meaning that whenever the starting conditions are slightly altered, the results of the system are vastly different while maintaining a seemingly random result.
This is ideal for encryption as encryption is essentially just taking input and modifying it with a key that makes it indiscernible from the input, while still being able to be decrypted with another key. To ensure security, the encrypted output should look random and different from the input. 

Diffie-Hellman key exchange protocol

	The Diffie-Hellman key exchange protocol is a key exchange protocol that allows for a shared key to be generated between two different parties. This system allows the two parties to have a shared key to encrypt media, without having to transmit the shared key. This works by having each party have a private and public key. 
The sender uses their public key to start the generation of the shared key. Each party, starting with the public key, combines the common public key with their secret key. They then exchange these combined values. With the other party’s combined value, they then add their private key to the combined value. At this point, they now have a shared key, without publicly exchanging it. 

	Figure 1

Shown in figure 1 is a good visualization of the process of creating a shared key, with paint [2]. The assumption implicit in the figure is that trying to separate the colours to determine the initial colours is extremely difficult and computers cannot calculate it fast enough. 
This process, although slower than establishing a shared key by somehow agreeing on a shared key before communication, allows for two parties to create a shared key without having to reveal any sensitive information. This key exchange is used in many modern security protocols online. 

Logistic map

The logistic map is a polynomial mapping that was originally designed as a population model. The map is mathematically described as
Xn+1=rXn(1-Xn)

Xn is a number between 0 and 1 and it is the ratio between the existing population to the maximum possible population. 

r represents the growth rate of the population. For chaotic behaviour to exhibit itself, the value of r must be between the ranges of 3.57 to 4.

This mathematical map is shown to have chaotic behaviour. This is one of the most studied chaotic systems, as it is quite simple. 

Cyclic shifts

Cyclic shifts are when you take values from a list and move them to the back. It is best demonstrated by an example. 
We have a list A = [1,2,3,4]
Then we want to cyclically shift A to the left by 1. 
This would result in A= [2,3,4,1]
If we were to shift A again to the left by 1, the result would be:
A=[3,4,1,2]
Now, if we were to shift A to the right by 1, we would get:
A=[2,3,4,1]
 

Pseudorandom number generator

A pseudo-random number generator, abbreviated as PRNG, is an algorithm that accepts an initial seed that may contain truly random values. The algorithm then generates values that appear to be random based on the initial seed. One of the most important characteristics of a PRNG is that it will produce the same result if the same initial seed is used.
In contrast to true random number generators, which use a source of true randomness, a PRNG uses a defined mathematical process to generate values that appear to be random. 
Although the values generated by a PRNG are not random, they should appear random, and statistically, they should appear random. A PRNG’s "randomness" can be tested using a variety of statistical tests.
Because of their reproducibility and speed, PRNGs are used in place of true random number generators.
PRNGs are often created with a recursive process. Essentially what this means is that once the PRNG generates a value, the value is then used to derive a new seed to pass through the generator again. The state of the generator is the current value that the generator is using.

Cryptographically secure pseudorandom number generator

	Cryptographically secure pseudorandom number generators, abbreviated as CPRNG, are the same as pseudorandom number generators with a few extra requirements; they must pass the next bit test, and withstand state compromises. 
	The next bit test is described as given, for the first k bits of a random sequence there is no polynomial time algorithm to predict the (k+1)th bit with a probability of success of better than 50%. [3]
	A state compromise is when the current state of the PRNG is jeopardized and a part of its entire state is exposed. To withstand such a compromise, even when the state is exposed, the attacker should not be able to reveal the previous or future values generated by the PRNG. 

Cryptographic hashes

 Cryptographic hashes are the output of hashing an input. Hashing is the process of transforming an input of any length, to a “hash” of fixed length. For a hashing algorithm to be successful, it must fulfil certain requirements:
Deterministic. If the same input is hashed more than once, it should always result in the same hash. 
The hash function is 1-way. Given the hash of some input, backtracking to try and determine the input should be infeasible.
There should not be any collisions between hashes. What a collision means is that multiple different inputs result in the same hash. 
It should be noted that all hash functions will have some collisions, as there is an infinite number of inputs, but a finite set of possible outputs. 	
A cryptographic hash uses an avalanche effect to create the hash. What this means is that any small changes in the input will snowball, and “avalanche” into a very different output. 

Perceptual hashing

Contrary to the definition above, perceptual hashes, use a locality-sensitive hash. What this means is that the hash is generated by grouping similar items into the same “buckets” to generate the hash [5]. What this means is that you can use this perceptual hash to find similarities between 2 images.

Chebyshev Polynomials

The Chebyshev polynomials consist of two different sequences, the Chebyshev polynomial of the first kind, and the second kind. They can be described in many different ways, but the recurrence relation is shown below.
Tn+1(x)=2xTn(x)-Tn-1(x)
T0(x)=0
T1(x)=x

Un+1(x)=2xUn(x)-Un-1(x)
U0(x)=0
U1(x)=2x

The recursive relations are identical, except for the starting values in which the Chebyshev polynomial of the first kind has T1(x)=x, and the Chebyshev polynomial of the second has U1(x)=2x.


Chosen plaintext attacks

A chosen plaintext attack (abbreviated as CPA) is an attack that assumes that the attacker can obtain the ciphertext for a plaintext of their choosing. With this information, the attacker attempts to reveal all or part of the key used for encryption. 
This attack proves to be impossible to defend against for deterministic algorithms. A deterministic algorithm is when the output of the algorithm is always the same, with the same input. This can be boiled down to the fact that it allows the attacker to determine whether two ciphertexts encrypt the same plaintext. A good analogy for this is, sealed envelopes, you shouldn’t be able to tell whether the envelopes contain the same thing. [4] 
Security against what was described above is called indistinguishable under chosen plaintext attack (abbreviated as IND-CPA). The attack that would be used to exploit this is shown below:
Challenger generated a shared key (SK) and a public key (PK). PK is shared with the adversary, and SK is kept secret.
The adversary then chooses different plaintexts, M0 and M1, and sends them to the challenger.
The challenger, picks a random value b, b{0,1}, at random. The challenger then encrypts Mb with PK and sends it back to the adversary.
The adversary returns a guess for the value b. 

	Something is IND-CPA if the adversary has no advantage over random guessing for b. If something is IND-CPA, then it is also immune to CPA. 

Entropy

Entropy, in this case, is being described in the context of information theory. Entropy can be abstracted to being a measurement of the uncertainty of a random variable. Entropy can be measured in different ways, however, the focus here is on Shannon’s entropy. The formula for Shannon’s entropy is described below:

H(x)=-xp(x) log2(p(x))
Where p(x) is the measure of the probability of an event happening. In the context of calculating the entropy of an image, the equation can be slightly modified, as shown below:

H(M)=-i=0255p(Mi) log2(Mi)
Where i represents the value of the pixel, which ranges from 0-255.
p(Mi) represents the frequency of pixels with value i in image M

To calculate the entropy of an RGB image, the formula above would be used for each colour channel. 

The maximum entropy of an image is dependent on the number of unique pixel values that are present in the image. The specific equation is shown below:

max(H)=log2(n)
n represents the number of unique pixel values in the image. For example, in an image where all 255 possible R,G,B values are present in the image, the maximum entropy for the image would be 8. 






IV. Design

The overall design plan for the encryption process of the algorithm is shown in Figure 2. The decryption process is shown in Figure 3. 

Figure 2


Figure 3

This is the overall design of the encryption algorithm. Each step will be covered in more depth in section VI. 


V. Design criteria

The encryption algorithm proposed must meet the following criteria:
The encryption process should not take over 10 seconds 
The PRNG used must appear to be random
The encryption algorithm is CPA resistant
The algorithm must output different ciphertexts when encrypting the same input more than once. 
The encryption algorithm can encrypt both text and images.
High image entropy

VI. The proposed algorithm

Key exchange and generation

The key exchange and generation portion of the algorithm can be shown in the following flow charts. The key exchange system here is the same as described in [1,7]. The key exchange system mimics that of the Diffie-Hellman key exchange. 

Figure 4 describes the generation of Bob’s private and public key. More in-depth steps are shown in algorithm 1. 


Figure 4

Algorithm 1:

Generate a random k-bit prime number p
Generate a large random number, sk
Generate a random number x
Public key = (p,x, Tsk(x) mod p, Usk-1(x) mod p)
Private key = sk
Tn(x) represents the Chebyshev polynomial of the first kind
Un(x) represents the Chebyshev polynomial of the second kind. 
Both the generation of the shared key for the other party (Alice) and the values to be sent to Bob are shown in Figure 5. It is described more in-depth in algorithm 2.

Figure 5

Algorithm 2:

Bob’s public is represented as (p,x,t,u)
Generate a large random number  as the ephemeral key
The shared key is calculated as (Uek-1(t) mod p)*u mod p
The values to be sent to Bob, so he can generate the shared key are shown as follows. Value to send to Bob = (Tek(x) mod p, Uek-1(x) mod p)
The process for calculating the shared secret for Bob is shown in Figure 6. A more in-depth description of the process is shown in algorithm 3. 


Figure 6

Algorithm 3:
The value sent from Alice to Bob is represented as (Tek,Uek)
Calculate Z = Usk-1(Tek) mod p
Shared key = (Z*Uek) mod p

Pseudorandom number generator

How the pseudorandom number works can be seen through the flow chart, shown in Figure 7. A description going into more detail is shown in Algorithm 4. This PRNG uses a logistic map, to calculate the pseudorandom values. The use of hashes and calling back to previous values in the list is what allows this PRNG to withstand state compromise.

Figure 7

Algorithm 4:
This process is for values that are not the first in the list. 
Initial values passed through the PRNG are X0,r,i
Calculate the value when passing these parameters through the logistic map. This will be called Z
Call back the previous random value and let it be Q. Then apply an XOR between these values, and call it G. G = Q xor Z
Apply a hash to G. This will result in a hexadecimal value. Convert the hexadecimal value into an integer. G= hexadecimal to integer (hash(G))
Truncate G accordingly and add it to the list of random values. 
From here, G is hashed and converted to an integer again. This new value is then used to create the new values for X0,r, i for the next iteration
As mentioned above, the hashing process is to withstand a compromised state.  Two values in the internal state of the PRNG could be compromised, either the seed values, X0,r,i, or the current sequence.
 If the current sequence is revealed to an attacker, there are two defences. First of all, it relies on the previous value in the sequence to generate a new value. However, if it weren’t for the hash, I believe it would be possible for an attacker to determine the previous value. Despite that, with the hash, an attacker cannot determine what the previous value would be, as the hash is 1-way, and you cannot determine the input. 
	If the current seed values are revealed to an attacker, the hashing process prevents the attacker from determining the previous value in the list, which in turn protects all future values generated. 

Text-to-image converter

	The process for converting text to an image is shown in Figure 8 and is described more in-depth in algorithm 5.

Figure 8

Algorithm 5
Calculate the size of the image. Size= Length of text/3 
Pad random values to the text, until its length, is equal to Size2*3. If the length of the text is already equal to Size2*3 then random values are padded to the text until it is equal to Size2*6
Go through the message and split it into chunks of 3. Encode these chunks of 3 into pixels. Then save the list of pixels into an image. 
The PRNG takes in 6 parameters, two of them being optional. The parameters are as follows:  X0, r, i, the number of values to be generated, which value should be returned in the list of random values, and the number of digits of values generated.


Encryption

	The encryption process of the algorithm can be split into two steps. The generation of the sequences for the encryption and the encryption itself. The sequence generation is shown in Figure 9 and is described more in-depth in algorithm 6. The encryption process is shown in Figure 10 and is explored more in algorithm 7. 


Figure 9

Algorithm 6:
Take the input image, and calculate the hash. This will be denoted as H
The Nonce is calculated by passing certain parts of the public key through the PRNG. The nonce will be denoted as N
The public and shared keys will be denoted as pk and sk respectively
H, N, pk and sk will all be XOR’ed together, to obtain a new value, which will be denoted as M.
The hash of M will be determined and then converted back into an integer. 
From here M will be split into 4 equal parts. If it cannot be broken down completely evenly, the last part will be slightly shorter.  Each of these 4 parts will be denoted as seed 1, seed 2, seed 3, and seed 4.
Each of these seeds will then be split and modified to make them suitable to pass through the PRNG as parameters. 
Each of these seeds will be passed through the PRNG, and generate 4 sequences which will be called, A, B, C and D. 


Figure 10

Algorithm 7:

The first step is to create new pixel values. This is done by going through each RGB value in each pixel of the image and creating a new pixel value by taking the location of each pixel, matching them up with values in the random sequence and then XORing them together. The pseudo-code for this is shown below:

For i = 0…image size:
	For j = 0…image size:
		For k = 0…3:
			newValue = (A[i] XOR B[k] XOR D[k]) mod 256
			newValue= | Image[i,j,k] XOR newValue |
			Image[i,j,k]=newValue
The second step is to shuffle the rows of the image. This is done by getting random values from one of the sequences, and calculating how many times the row should be cyclically shifted to the left. This results in each row being shuffled and the order is changed. The pseudo-code for this is shown below:

For a = 0…image size:
	Shifting value = D[a] mod image size
	Current row= row a in image
	New row= current row shifted to left by shifting value
	Row a in image= New row
The third step is to shuffle the columns of the image. This is done in the same way as above, but with each column. The pseudo-code for this is shown below:

	For a = 0…image size:
		Current column= column a in image
		Shifting value = A[a] mod image size
		New column = current column shifted to left by shifting value
		Column a in image = new column
The final step is to shift each pixel value. What this means is that each R, G and B value of each pixel will be shifted in the same way as above. The pseudo-code for this is shown below:
	
	For row in image:
		Current r values = all r values in the row
		Shifting value = A[row number] XOR C[0] mod size
		New r values = Current r values shifted to the left by shifting value
		
		Current g values = all g values in the row
		Shifting value = A[row number] XOR C[1] mod size
		New g values = Current g values shifted to the left by shifting value

		Current b values = all b values in the row
		Shifting value = A[row number] XOR C[2] mod size
		New b values = Current b values shifted to the left by shifting value

		New row = combining new r values, new g values and new b values 
		Image[row number] = new Row
		

Decryption

	The decryption process is identical to that of the encryption process, the only difference being that the values are cyclically shifted to the right and the steps are reversed. The overall process is shown in Figure 11, and a more detailed explanation is shown in algorithm 8. It should be noted that when the encrypted image is sent to the other party, they also send the image hash and nonce together with the image. This is to allow the other party the ability to decrypt it. This doesn’t hinder security, as all of those values are public, and the hash is secure and won’t reveal the original image. 


Figure 11

Algorithm 8:

The first step is to shift each pixel value. What this means is that each R, G and B value of each pixel will be shifted in the same way as above. The pseudo-code for this is shown below:
	
	For row in image:
		Current r values = all r values in the row
		Shifting value = A[row number] XOR C[0] mod size
		New r values = Current r values shifted to the right by shifting value
		
		Current g values = all g values in the row
		Shifting value = A[row number] XOR C[1] mod size
		New g values = Current g values shifted to the right by shifting value

		Current b values = all b values in the row
		Shifting value = A[row number] XOR C[2] mod size
		New b values = Current b values shifted to the right by shifting value

		New row = combining new r values, new g values and new b values 
		Image[row number] = new Row

The second step is to reorganize the columns of the image. The pseudo-code for this is shown below:

	For a = 0…image size:
		Current column= column a in image
		Shifting value = A[a] mod image size
		New column = current column shifted to the right by shifting value
		Column a in image = new column

The third step is to reorganize the rows of the image. The pseudo-code for this is shown below:

For a = 0…image size:
	Shifting value = D[a] mod image size
	Current row= row a in image
	New row= current row shifted to the right by shifting value
	Row a in image= New row

The final step is to restore the old pixel values of the image. The pseudo-code for this is shown below:

For i = 0…image size:
	For j = 0…image size:
		For k = 0…3:
			newValue = (A[i] XOR B[k] XOR D[k]) mod 256
			newValue= | Image[i,j,k] XOR newValue |
			Image[i,j,k]=newValue

VII. Testing and testing results

There were seven main tests used to evaluate this encryption algorithm. Each of these tests will be covered in-depth and the results will be shown and compared to other chaotic algorithms. The first four tests were used to evaluate the utility and practicality of the encryption algorithm. The final two tests are to evaluate the randomness of the PRNG. 

Key sensitivity

	This test is used to verify that chaos does exist in this algorithm; if there is a slight change in initial conditions, the result will be completely different. The steps used to perform this test are shown in test 1. This test is run 100 times, separately for images and texts.
Shown below in Figure 15, is the graph of similarity values for encrypted images. The image used for the encryption and decryption process is shown in Figure 14. The graph for similarity values for encrypted text is shown in Figure 16. 

Test 1:
Generate a shared key, Sk
Encrypt any type of media with the key Sk
Decrypt the encrypted image with Sk-1
Calculate the similarity between the 2 images with perceptual hashing
The similarity value can vary, but as a baseline, the similarity value between Figures 12 and 13 is 52. The text for encryption is “ABCDEFGHIJKLMNOPQRSTUVWXYZ”


Figure 12


Figure 13



Figure 14



Figure 15



Figure 16

Information entropy analysis 

This test is used to calculate the entropy of the images this algorithm encrypts. The test procedure is quite simple and is described in test 2. 
The results of this test are shown in Figure 17. Since in each image, there are 255 unique values for each pixel, the maximum entropy value is 8. 

Test 2:
Separate all the pixel values into three separate lists, each of them representing the R, G and B values of the pixels. The three lists will be denoted as R,G,B
The frequency for each value in R,G,B will be calculated. This frequency will be denoted as P
The entropy for each colour channel will be calculated as shown in this equation: -p*log2(p)
You would use the equation for each list, R,G,B


Media input
Encrypted output
Entropy values


Max value
R
B
G
Average






7.99990
7.999896
7.999904
7.999901


8


7.999824
7.999839
7.999827
7.999830


8


7.999932
7.999927
7.999931
7.999930


8
“ABCDEFGHIJKLMNOPQRSTUVWXYZ”

4.0
4.0
3.75
3.916667


4

Text 1

7.935641
7.912595
7.906195
7.918144


8
Text 2

7.991143
7.992013
7.993236
7.992131


8

Figure 17


Histogram analysis

This test is to evaluate whether or not the encryption algorithm would be prone to statistical attacks. This is done by creating a histogram of the frequency of each pixel colour. If the histogram is flat, it means that the encryption algorithm is immune to statistical attacks, as all the values are equally distributed. A more in-depth look at the test is shown in test 3. 
The result of the test is shown in Figure 18.

Test 3:
For each colour channel, R, G,B, count how many times it appears in the image.
Take these values and plot them into a histogram. 

Image
R
G
B
Encrypted output
R
G
B
























“ABCDEFGHIJKLMNOPQRSTUVWXYZ”








Text 1







Text 2








Figure 18


Sensitivity analysis

	This test is to evaluate how chaotic the algorithm is when it encrypts media. This is done by using perceptual hashing to calculate the difference between two encrypted images. Both of these encrypted images are encrypted with the same image and with the same keys. The only difference is the random padding that is used. More details are shown in test 4. This test is run 1000 times, separately for text and images. 
Shown in Figure 19, is the image for encryption. Figures 20 and 21, show the graph of similarity, for image and text respectively. The image used for encryption had been scaled down as the tests would have taken too long to run. The text used for the encryption is “ABCDEFGHIJKLMNOPQRSTUVWXYZ”

Test 4:
Take an input, and encrypt it twice. The two encrypted images will be denoted as M0 and M1
Calculate the image similarity value between M0 and M1


Figure 19


Figure 20



Figure 21



Speed test

	This test is used to evaluate the speed of the proposed algorithm. It's a very simple test, I simply compare the run time of encrypting the input to the size of the input in bytes. A different key is used every time. There is no need for a more in-depth description of this test, as it is very straightforward. 
The table showing the data is shown in Figure 22, and the resulting graph is shown in Figure 23. 


Input size in bytes
Try 1
Try 2
Try 3
Average
26
0.481107
0.460835
0.476704
0.472882
100
0.496990
0.470051
0.519193
0.495411
1,000
0.678098
0.679956
0.674632
0.677562
10,000
1.363886
1.310424
1.4116724
1.361994
100,000
3.634213
3.931432
3.617568
3.727738
700,000
10.062586
10.180218
9.964787
10.069197


1,000,000
12.615493
12.470045
12.37008
12.485206


Figure 22


Figure 23


Information entropy analysis on the PRNG

	This test is the same as the information entropy analysis on the encryption algorithm, the only difference being that it is run on the values generated by the PRNG. A look into each step is shown in test 5.
	The results of this test can be shown in Figure 24

Test 5:
Generate X values from the PRNG
Take each value generated and mod it by 256. This is done to limit the possible values to 0-255
For each value generated, calculate its frequency in the list. This will be denoted a P
Calculate the entropy with the equation below:
-i=0255p*log2(p)


Initial conditions
Number of Sample Extracted
10000
20000
40000
60000
80000
100000
200000
X0=0.5
R=3.8
I=1000
7.98261
7.99159
7.99605
7.99719
7.99782
7.99816
7.99907
X0=0.9734
R=3.9748
I=6736
7.981748
7.990844
7.995732
7.997161
7.997822
7.998245
7.999062	
X0=0.6942
R=3.6779
I=8459
7.978881
7.989655
7.995113
7.996546
7.9976
7.998034
7.998973
X0=0.1674
R=3.7166
I=7348
7.98206
7.990617
7.994789
7.996493
7.99758
7.997997
7.999032

Figure 24


PRNG sensitivity analysis

	This test is used to ensure that the PRNG used is chaotic and sensitive to initial conditions. The way this test is run is by slightly changing the initial seed of the PRNG, waiting and for a different result. This reveals at what decimal place for each parameter the PRNG becomes chaotic.
The table of data for the results on shown in Figure 25. 


Parameter tested
Value of change
Other parameters
X0
1*10-14
R=3.8, i=1000
1000 values generated
R
1*10-15
X0=0.5, i=1000
1000 values generated
I
1
X0=0.5, R=3.8
1000 values generated

Figure 25

 

VIII. Security analysis

	This encryption algorithm proves to perform better than other chaotic encryption algorithms similar to it. In [1], there is a list of different papers and their results for the information entropy test and this algorithm fairly consistently performs better in this test, when encrypting similar inputs. 
	When comparing the PRNG results with a similar PRNG, the PRNG described in this paper [6], consistently performs better once there are 40,000 samples generated. For any number of samples under 40,000 for certain initial conditions, the PRNG described in this paper performs better, but not for others. 
	When looking at the graphs of the similarity values, in Figures 15, 16, 20 and 21, the correlation values for the graphs are 0, or at least very close to 0, which indicates negligible correlation.  This is good as it means, even as the number of encrypted values grows and the similarity is calculated, all the values stay consistently different. 
	When running the histogram test, the results are quite promising, the encrypted image tends to have a completely flat distribution of values, which means that this algorithm is not vulnerable to statistical attacks.
	Regarding the sensitivity analysis of the PRNG, it is extremely sensitive to its initial conditions. Such minuscule changes result in a completely new sequence being generated. This further strengthens the algorithm against any possible brute-force attacks. 
	The randomized aspect of the algorithm combined with the chaotic behaviour of the algorithm that it displays, it can be said that this algorithm is CPA-secure. 
	



IX. Conclusion and application

	The proposed algorithm in this paper, proved to be quite secure, CPA-secure, and managed to outperform similar algorithms. Through the testing, it can be concluded that this algorithm, is quite secure, and demonstrates that chaos-based encryption can be implemented and used successfully. 
	As for the application of this algorithm, this can be used for encryption as it is quite secure as mentioned in the security analysis. This essentially acts as a proof of concept for chaotic encryption. It presents a successful chaotic encryption algorithm. 

X. Next steps

	There are a few things that can be improved on for this algorithm. The main limiting factor of this algorithm is its speed. This algorithm was written in python, which by its nature is a slow language. Essentially,  to improve this algorithm, writing it in another faster coding language might be beneficial. Secondly, more vigorous testing can be done on the algorithm to try and find any possible weaknesses. 

XI. Appendix

Appendix A: Text used for testing


Text 1: 
https://docs.google.com/document/d/1wTlsgGgT6JjX3XoMy0VKHK1jidelAUixA9Woga-NtYE/edit?usp=sharing

Text 2:
https://docs.google.com/document/d/1KeyFLhetCBs5CeEc6vd_TUJIgJ9aP_mOskdqcb8B-0Y/edit?usp=sharing

Appendix B: Construction log

The log for the construction of this algorithm is in this document: https://docs.google.com/document/d/1mAxP8LAFmqSebK4_IsYJbWbloubKHIyyoBByyD5lpPY/edit?usp=sharing

Appendix C: Python packages

The list of python packages used to create this algorithm:
Pillow
Numpy
Hashlib
Random
Csv
Math
Matplotlib
imageHash
Collections 

Appendix D: GitHub repository

The GitHub for this project is in the link below. It contains all the code for the algorithm, and code to test it.
“link”


XII. Bibliography

[1] Shakiba, A. (2021). A randomized CPA-secure asymmetric-key chaotic color image encryption scheme based on the Chebyshev mappings and one-time pad. Journal of King Saud University - Computer and Information Sciences, 33(5), 562–571. https://doi.org/10.1016/j.jksuci.2019.03.003

[2] Diffie–Hellman key exchange. Wikipedia Contributors. (2019, December 10). Wikipedia; Wikimedia Foundation. https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange

[3] Cryptographically secure pseudorandom number generator. (2021, April 17). Wikipedia. https://en.wikipedia.org/wiki/Cryptographically_secure_pseudorandom_number_generator

[4] 7 Security Against Chosen Plaintext A acks. (n.d.). https://joyofcryptography.com/pdf/chap7.pdf

[5] Perceptual hashing. (2021, December 4). Wikipedia. https://en.wikipedia.org/wiki/Perceptual_hashing

[6] Wang, L., & Cheng, H. (2019). Pseudo-Random Number Generator Based on Logistic Chaotic System. Entropy, 21(10), 960. https://doi.org/10.3390/e21100960

[7] Fee, G., & Monagan, M. (n.d.). Cryptography using Chebyshev polynomials. http://wayback.cecm.sfu.ca/CAG/papers/Cheb.pdf

[8] Lawnik, M., & Kapczynski, A. (2019). The application of modified Chebyshev polynomials in asymmetric cryptography. Computer Science, 20(3), 367. https://doi.org/10.7494/csci.2019.20.3.3307

[9] Wikipedia Contributors. (2019, November 7). Chebyshev polynomials. Wikipedia; Wikimedia Foundation. https://en.wikipedia.org/wiki/Chebyshev_polynomials

[10] Weisstein, E. W. (n.d.). Chebyshev Polynomial of the First Kind. Mathworld.wolfram.com. https://mathworld.wolfram.com/ChebyshevPolynomialoftheFirstKind.html

[11] Weisstein, E. W. (n.d.-b). Chebyshev Polynomial of the Second Kind. Mathworld.wolfram.com. https://mathworld.wolfram.com/ChebyshevPolynomialoftheSecondKind.html

[12] Wikipedia Contributors. (2019a, November 5). Miller–Rabin primality test. Wikipedia; Wikimedia Foundation. https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test

[13] Wikipedia Contributors. (2019a, October 11). Logistic map. Wikipedia; Wikimedia Foundation. https://en.wikipedia.org/wiki/Logistic_map

[14] Pseudorandom number generator. (2021, September 22). Wikipedia. https://en.wikipedia.org/wiki/Pseudorandom_number_generator

[15] Cryptographically secure pseudorandom number generator. (2021, April 17). Wikipedia. https://en.wikipedia.org/wiki/Cryptographically_secure_pseudorandom_number_generator

[16] Lawnik, M., Pełka, A., & Kapczyński, A. (2020). A New Way to Store Simple Text Files. Algorithms, 13(4), 101. https://doi.org/10.3390/a13040101

[17] Ciphertext indistinguishability. (2020, October 27). Wikipedia. https://en.wikipedia.org/wiki/Ciphertext_indistinguishability

[18] Cryptographic nonce. (2021, December 26). Wikipedia. https://en.wikipedia.org/wiki/Cryptographic_nonce

[19] Image Module — Pillow (PIL Fork) 6.2.1 documentation. (2011). Readthedocs.io. https://pillow.readthedocs.io/en/stable/reference/Image.html

[20] NumPy Documentation. (n.d.). Numpy.org. https://numpy.org/doc/

[21] Chosen-plaintext attack. (2021, October 20). Wikipedia. https://en.wikipedia.org/wiki/Chosen-plaintext_attack

[22] Wikipedia Contributors. (2019a, April 2). Entropy (information theory). Wikipedia; Wikimedia Foundation. https://en.wikipedia.org/wiki/Entropy_(information_theory)

[23] Introduction to Information theory Measuring Uncertainty and Information. (n.d.). Retrieved February 25, 2023, from http://www2.hawaii.edu/~sstill/ICS636Lectures/ICS636Lecture2.pdf

