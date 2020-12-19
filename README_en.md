Number of GS

In this readme, i'm going to explains you how i get the idea for this cipher and how its work.

For every chipher, you need to respect the confidentiality, authenticity and integrity but mine is just a little one for training so i just thinking about confidentiality.

Then I had an idea from a friend who one day made me pass a test for iq. I took that to make the main calcul for the encryption. There is an example:

```
12 + 8 = 204
25 + 11 = 3614
6 + 5 = 111
9 + 7 = ?
```

If you want to pass the test, you have 3 minutes to solves this ;) (and stop reading, you will be spoiled)

Solution = 162
It's quit simple, you just need to make 9 + 7 = 16 and 9 - 7 = 2 and then compute them together: 162

So my idea is to convert the message into an integer and take each bit seperatly into a list and compute the first bit with next one and that every two bits until the end of the block:
```
message = "cipher"
int_m = "109304508605810"
my_block = ['1', '0', '9', '3', '0', '4', '5', '0', '8', '6', '0', '5', '8', '1', '0']
cipher = f(my_block[i], my_block[i+1])

e.g: (1+0) + (1-0) = 11
```

Important: the block[i] need to be greatest than block[i+1] because 4 + 9 = 13 but then 4 - 9 = -5 and we dont want it !
If block[i+1] > block[i], you need to pass those two numbers into a function to switch them.

Important: In my algorithm, you can see a key wich return some 0 and 1, this represents the switching. 1 == switching, 0 == no switching.
For the moment we can't decrypt the message with it so the key isn't really important for know.

Then, I decided to make it a little bit more tricky and complexe by making this operation until the len of my block equal 1.
Be careful, if the len of the block isn't peer, the algorithm wouldn't work, because you can compute an number with nothing 
(e.g: ['137115', '9911', '19787', '9797'] working
      ['137115', '9911', '19787']         not working)

```
message = "cipher"
['1', '0', '9', '3', '0', '4', '5', '0', '8', '6', '0', '5', '8', '1', '0']
['1', '0', '9', '3', '0', '4', '5', '0', '8', '6', '0', '5', '8', '1', '0', '0']    #As you can see, the len of the block isn't peer, so i add a 0.
['11', '126', '44', '55', '142', '55', '97', '00']
['137115', '9911', '19787', '9797']
['147026127204', '295849990']
cipher = ['147321977194146730277214']
```

So my cipher allow to encrypt any text wich can be convert into integer, the algorithm can encrypt any blocks only if the len is peer, else, the algorithm will add 0 as padding. The outpout of the algorithm have a variable len but I work on it to optimize the size wich can become very big.
For the moment you can only be sur that the ciphertext cant be read.

For the next upload:
So for decrypting a message, you need to find the last two numbers wich gave the cipher (['147026127204', '295849990']), then the four numbers wich gave the two numbers before the cipher and you continu until the end to find the message and convert him in bytes.
I'm actually coding a function wich can do this operation, I will post it soon as possible !

If you have some advices or questions, please tell me on discord or twitter !
