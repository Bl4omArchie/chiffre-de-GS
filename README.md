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
Faites attention, si la taille du bloc n'est pas pair, l'algorithme ne marchera pas car on ne peut pas additionner un nombre avec rien !
(exemple: ['137115', '9911', '19787', '9797'] working
          ['137115', '9911', '19787']         not working)

```
message = "cipher"
['1', '0', '9', '3', '0', '4', '5', '0', '8', '6', '0', '5', '8', '1', '0']
['1', '0', '9', '3', '0', '4', '5', '0', '8', '6', '0', '5', '8', '1', '0', '0']    #Comme la taille du bloc n'est pas pair, j'ai ajouté un 0.
['11', '126', '44', '55', '142', '55', '97', '00']
['137115', '9911', '19787', '9797']
['147026127204', '295849990']
cipher = ['147321977194146730277214']
```
Donc mon cipher permet de chiffrer n'importe quel text qui peut être converti en entier. L'algorithme peut chiffrer n'importe quel bloc à la seule condition que sa taille soie paire sinon l'algorithme ajoute un 0 au bloc. La sortie de l'algorithme a une taille qui est variable mais je travaille dessus pour optimiser le taille car elle peut, en fonction du message, devenir très grande.
Pour le moment, on ne peut que être sur que le message ne peut être lu.

Pour la prochaine maj:
Donc pour déchiffrer un message il faut trouver les deux derniers blocs qui donne le ciphertext final (['147026127204', '295849990']), puis les quatres autres blocs qui ont donné ces deux là et ainsi de suite jusqu'à ce que l'on trouve le message original composé d'un seul bloc.
Je travaille sur cette fonctione qui permettrait de déchiffrer !

Si vous avez des questions ou des conseils, n'hésitez pas à me le faire savoir sur twitter ou discord !
