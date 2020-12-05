# Chiffre de GS/ number of GS

In this readme, i'm going to explains you how i get the idea for this cipher and how its work.

For every chipher, you need to respect the confidentiality, authenticity and integrity but mine is just a little one for training so i just thinking about confidentiality.
I also wanted to make a cipher wich return a ciphertext very small to be very optimize with a small key too.

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

So my idea is to convert the message into an integer, split the result into a list and make this calcul with the next case of the list:
```
message = "cipher"
int_m = "109304508605810"
list = ['1', '0', '9', '3', '0', '4', '5', '0', '8', '6', '0', '5', '8', '1', '0']
cipher = f(list[i], list[i+1])

e.g: (1+0) + (1-0) = 11
```

I decided to make it a little bit more tricky and complexe by making this operation until there’s only one place left in my list.

```
message = "cipher"
['1', '0', '9', '3', '0', '4', '5', '0', '8', '6', '0', '5', '8', '1', '0']
['1', '0', '9', '3', '0', '4', '5', '0', '8', '6', '0', '5', '8', '1', '0', '0']
['11', '126', '44', '55', '142', '55', '97', '00']
['137115', '9911', '19787', '9797']
['147026127204', '295849990']
cipher = ['147321977194146730277214']
```

So for now, for decrypting a message, you need to find the last two numbers wich gave the cipher (['147026127204', '295849990'])

Note: This is only some test, nothing is done know ! And also in the implementation of my cipher, the key isn't really important know, for the moment i work on the decryption so I didn't define precisely what the key is going to be.

