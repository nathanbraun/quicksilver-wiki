
# Stephenson:Neal:Quicksilver:641:Wilkins cypher (Neal Stephenson)

From the Quicksilver Metaweb.

Starting on p. 88 of his book *Mercury*, [Wilkins](/john-wilkins) explains a [steganographic](/steganography) cypher based on what we would identify as binary numbers. The key to this cryptosystem is the use of two different handwritten alphabets, denoted (somewhat confusingly) the "a" alphabet and the "b" alphabet. I will call them the 0 alphabet and the 1 alphabet instead, or else this description will be difficult to make sense of. The letters of both alphabets look more or less normal, and are easily readable, but a letter "m" from the 0 alphabet is distinguishable from a letter "m" from the 1 alphabet, and the same is true of all of the other letters. The sender writes a normal-looking message, but groups the letters of the ciphertext into blocks of five, and within each block of five, chooses each letter from either the 0 alphabet or the 1 alphabet. The recipient, upon scrutinising the individual letters, can translate the message into a sequence of five-digit binary numbers. These can then be converted to letters of the alphabet, yielding the plaintext message, which is only one fifth as long as the ciphertext message.

This form of cryptography was first suggested by [Francis Bacon](/francis-bacon); 
"WHEELE-CYPHARS, KAY-CYPHARS, DOVBLES, &c. But the vertues of them, whereby they are to be preferred, are three; that they be not laborious to write and reade; that they bee impossible to discypher; and in some cases, that they bee without suspition. The highest Degree whereof, is to write OMNIA PER OMNIA; which is vndoubtedly possible, with a proportion Quintuple at most, of the writing infoulding, to the writing infoulded, and no other restrainte whatsoever."
Bacon proposed using two closely related printed alphabets;
First let all the Letters of the Alphabet , by transposition, be resolved into two Letters onely; for the transposition of two Letters by five placeings will be sufficient for 32. Differences, much more for 24. which is the number of the Alphabet . The example of such an Alphabet is on this wise.

An Example of a Bi-literarie Alphabet.

[A (Aaaaa) ... Z (babbb)]

The matter is examined in detail in William and Elizabeth Friedman's The Shakespearean Ciphers Examined.

[Leibniz](/gottfried-wilhelm-von-leibniz) had an interest in binary numbers and was aware of Wilkins and his work. Here I am supposing that Leibniz invented a more powerful variant of Wilkins's cypher in which the five-digit binary numbers are further encrypted by adding to each one another binary number, which therefore serves as a key. The key is passed on in the plaintext message by means of a reference to one of the hexagrams of the I Ching (another one of Leibniz's real-life interests).

This cryptosystem is fictional, and as far as I know, nothing like it ever existed in the real world.

## Example



* Take two alphabets a(0) and a(1). The only difference between the two is that all letters in a(1) have a single quote following them (a', b', etc.).


* Write your cyphertext as follows:


 He'l'lo W'orl'd

* Break the cypher text into 5-letter words and translate each into a 5-digit binary number based on the alphabet each letter belongs to:


 01100 10010

* Now, add to each number the binary representation of an agreed upon (or enclosed) I Ching character, say 00001:


 01101 10011

* Finally, convert each binary number back into alphabetic characters:


 **M S**

Here it gets a little fuzzy. I assume that they'll do something like a = 1, b = 2, etc. But, because 2^5 - 1 = 31, and there are only 26 characters in the english alphabet, there are 5 untranslatable characters. But I can only assume that this can be explained away (or that I'm completely wrong).
(or - thinking of languages like German - one can use these for letters like ä, ö, ü, ß or such like)nb english is one of the only indoeuropean alphabets with 26 letters, 31 is a common number, it is correct to assume accented letters are counted as seperate letters in many languages. -c
