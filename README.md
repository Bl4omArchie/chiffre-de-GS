# Chiffre de GS

Dans ce readme, je vais vous expliquer d'où m'es venu l'idée de ce chiffrement et comment il fonctionne.

Pour tout chiffrement, nous devons respecter la confidentialité, l'authenticité et l'intégrité. Comme mon chiffrement n'est que pour m'entraîner et que j'en suis qu'au début, je vais d'abord me concentrer sur la confidentialité. 
L'idée m'es venu d'une amie qui un jour m'a fait passé un test de qi, l'épreuve était de comprendre une suite de calcul et la résourdre. Ca m'a insipiré et j'ai décidé d'en faire le calcul principal pour chiffrer avec mon système. 
Voici un exemple:

```
12 + 8 = 204
25 + 11 = 3614
6 + 5 = 111
9 + 7 = ?
```

Le test dur trois minutes si vous voulez faire ;) (Attention juste en dessous il y a la réponse)

Solution = 162
Il suffit juste de faire 9 + 7 = 16 et 9 - 7 = 2 on regroupe les deux resultats ce qui donnent 162.

Donc mon idée est de converti le message en entier, séparé chaque bit dans une liste et faire cette opération avec le premier et deuxième bit jusqu'à la fin du block et ceux tous les deux bits:
```
message = "cipher"
int_m = "109304508605810"
my_block = ['1', '0', '9', '3', '0', '4', '5', '0', '8', '6', '0', '5', '8', '1', '0']
cipher = f(my_block[i], my_block[i+1])

exemple: (1+0) + (1-0) = 11
```

Important: le block[i] doit être supérieur au block[i+1] sinon l'algorithme va retourner un nombre négatif, ce que nous voulons pas (ex: 4 + 9 = 13 mais 4 - 9 = -5)
Si block[i+1] > block[i], on passera alors ces deux nombres dans une fonction qui les échengeras.

Important: Dans le code vous pouvez voir la présence d'une variable clé qui retourne à la fin des 1 et des 0, ça représenter les échanges, 1 == échange, 0 == pas d'échange
Pour l'instant ne vous occupez pas de la clé, elle ne sert à rien.

Ensuite, j'ai voulu rendre l'algo un plus complexe en continuant l'opération jusqu'à ce que la taille du block soi egal à 1.
Be careful, if the len of the block isn't peer, the algorithm wouldn't work, because you can compute an number with nothing 
(exemple: ['137115', '9911', '19787', '9797'] working
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
