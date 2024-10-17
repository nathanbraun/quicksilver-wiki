
# The Vigenère Cipher (Talith)

From the Quicksilver Metaweb.

The Vigenère cipher was developed by Blaise de Vigenère (1523 - 1596), expanding on earlier work by Giovanni Porta, Leon Battista Alberti, and Johannes Trimethemius. It was first published in his book *Traicte des Chiffres ou Secretes d'Escrire* in 1586.

It uses a tableau of 26 substitution alphabets (the set of all possible [Caesar ciphers](/caesar-cipher)); it is a *polyalphabetic* cipher.



```
     A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
  ------------------------------------------------------
 A|  B C D E F G H I J K L M N O P Q R S T U V W X Y Z A
 B|  C D E F G H I J K L M N O P Q R S T U V W X Y Z A B
 C|  D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
 D|  E F G H I J K L M N O P Q R S T U V W X Y Z A B C D
 E|  F G H I J K L M N O P Q R S T U V W X Y Z A B C D E
 F|  G H I J K L M N O P Q R S T U V W X Y Z A B C D E F
 G|  H I J K L M N O P Q R S T U V W X Y Z A B C D E F G
 H|  I J K L M N O P Q R S T U V W X Y Z A B C D E F G H
 I|  J K L M N O P Q R S T U V W X Y Z A B C D E F G H I
 J|  K L M N O P Q R S T U V W X Y Z A B C D E F G H I J
 K|  L M N O P Q R S T U V W X Y Z A B C D E F G H I J K
 L|  M N O P Q R S T U V W X Y Z A B C D E F G H I J K L
 M|  N O P Q R S T U V W X Y Z A B C D E F G H I J K L M
 N|  O P Q R S T U V W X Y Z A B C D E F G H I J K L M N
 O|  P Q R S T U V W X Y Z A B C D E F G H I J K L M N O
 P|  Q R S T U V W X Y Z A B C D E F G H I J K L M N O P
 Q|  R S T U V W X Y Z A B C D E F G H I J K L M N O P Q
 R|  S T U V W X Y Z A B C D E F G H I J K L M N O P Q R
 S|  T U V W X Y Z A B C D E F G H I J K L M N O P Q R S
 T|  U V W X Y Z A B C D E F G H I J K L M N O P Q R S T
 U|  V W X Y Z A B C D E F G H I J K L M N O P Q R S T U
 V|  W X Y Z A B C D E F G H I J K L M N O P Q R S T U V
 W|  X Y Z A B C D E F G H I J K L M N O P Q R S T U V W
 X|  Y Z A B C D E F G H I J K L M N O P Q R S T U V W X
 Y|  Z A B C D E F G H I J K L M N O P Q R S T U V W X Y
 Z|  A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

```


To encipher a message using the Vigenère cipher, a keyword is chosen and any repeated letters removed. For example, 


```
 METAWEB

```

would be used as


```
 METAWB

```

The message to be enciphered is written out and the keyword is written below it, repeating it as many times as needed for the length of the message. Each pair of letters - one message letter and one keywords letter - is then used to look up the ciphertext letter within the tableau (since the table is symmetric it doesn't matter which letter is used to index the rows and which to index the columns). For example,


```
 Message: N E A L S T E P H E N S O N W R O T E C R Y P T O N O M I C O N
 Keyword: M E T A W B M E T A W B M E T A W B M E T A W B M E T A W B M E

```

gives

```
 
 Cipher:  A J U M P V R U B F K U B S Q S L V R H L Z M V B S I N F E B S

```

To decipher the message, you simply reverse the process; write the keyword out underneath the enciphered message and look up the corresponding letters in the tableau. The result will be the original message.

(An alternative tableau to the one above has the A row with no shift, i.e. starting with A. The layout given above makes more sense if you think about the positions of the letters within the alphabet, A = 1, B = 2, up to Z = 26; adding the positions of the letters whose row and column you are looking in gives you the position within the alphabet of the result. For instance, if you want the result of combining C and E; C is in position 3, E is in position 5, so the result should be in position 8; if you look at the table above, the result of combining C and E is H, which is indeed in position 8 within the alphabet.)

The Vigenère cipher is more secure than a simple (monoalphabetic) substition cipher because the same alphabet isn't being used throughout the enciphered message; in this case, six different alphabets are being used, because the keyword is six letters long. 

Unfortunately, despite the Vigenère cipher being seen as very hard to break, it was not widely used. A German variant, the Gronsfeld cipher, used digits of a key number rather than letters of a key word, and was more widely used (despite being generally weaker than the Vigenère cipher, because it had fewer substitution alphabets from which to choose).

The Vigenère cipher was considered almost impossible to break for several hundred years after its description. A method of attack was finally proposed by Kasiski in 1863. His method consisted of two parts; first, guessing the length of the keyword, and then attacking each of the component ciphers separately.

Kasiski's method for guessing the length of the keyword used involved measuring the distance between repeated [bigrams](/bigrams) in the ciphertext. For instance, in the ciphertext example above, the bigram **BS** appears three times, at positions 13, 25 and 31. Kasiski reasoned that a repeated bigram might be the same two letters of message text being enciphered with the same two letters of keyword - the factors of the distances between the repeated bigrams therefore giving a clue to the length of the keyword. In this case, the distances are 12 and 6, so you might therefore guess that the keyword used to encipher the message was of length 6 - and indeed this is the case. Every sixth letter within the ciphertext is enciphered with the same keyword letter. 

Grouping the ciphertext letters according to which letter of the keyword enciphered them (so, the 1st, 7th, 13th etc. in one group; the 2nd, 8th, 14th etc. in the next group, and so on), [frequency analysis](/frequency-analysis) can be used to ascertain which cipher was used to encipher each group, and thus the keyword can be recovered.
