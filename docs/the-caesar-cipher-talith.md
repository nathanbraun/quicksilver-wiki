
# The Caesar cipher (Talith)

From the Quicksilver Metaweb.

The Caesar cipher is a simple [substitution cipher](/substitution-cipher). It is named after [Julius Caesar](/julius-caesar), who is said to have used it to communicate within his army. 

The Caesar cipher is *monoalphabetic*, that is, the same substitution is used throughout the message. The ciphertext alphabet is shifted a certain number of letters to the right or left of the plaintext alphabet. To encipher a message, the plaintext alphabet is written out above the ciphertext alphabet; each letter of the message is looked up in the plaintext alphabet and the letter of the ciphertext which appears immediately below it is used within the enciphered message.

The 'Caesar shift', said to have been used by Caesar himself, shifts every letter three places to the right, so the plaintext and ciphertext alphabets look like this:


```
 Plaintext:  A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
 Ciphertext: D E F G H I J K L M N O P Q R S T U V W X Y Z A B C

```

and the message 

```
 
 BEWARE THE IDES OF MARCH

```

would be enciphered as


```
 EHZDUH WKH LGHV RI PDUFK

```

It is possible to use any letter shift between 1 and 25 letters to the left or right (1 letter to the right being equivalent to 25 letters to the left).

Breaking a Caesar cipher is usually achieved by means of [frequency analysis](/frequency-analysis). Because the whole message is enciphered using the same substitution alphabet, every enciphered letter will always correspond to the same letter in the plaintext message; in the example above, every H in the ciphertext corresponds to an E in the plaintext. If you have a ciphertext where the most frequent letter is D, for instance, it would be reasonable to try the shift where an enciphered D corresponds to a plaintext E (one letter to the left) first.
