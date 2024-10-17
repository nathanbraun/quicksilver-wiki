
# Frequency analysis (Talith)

From the Quicksilver Metaweb.

Frequency analysis is a method of cryptanalysis used in breaking simple [substitution ciphers](/substitution-ciphers). It can be applied to break monoalphabetic ciphers such as the [Caesar cipher](/caesar-cipher) and can also be used when a polyalphabetic cipher such as the [Vigenère cipher](/vigenère-cipher) has been broken up into its monoalphabetic components.

The basic idea behind frequency analysis is that, for any given language, the letters within that language tend to appear with roughly the same frequencies in any piece of text. In English, for example, the six most common letters are E T A O I N; in Spanish the six most common letters are E A O S R N; and in Latin the most common are I E U T A M. This can also be extended to [bigrams](/bigrams) and [trigrams](/trigrams) - the most common English bigrams are TH, HE, IN and ER.

To analyse a piece of ciphertext, the frequencies of the letters (or symbols) within it are calculated and the results compared to the frequency of letters occurring within the language in which the original message was written. So if the plaintext message was written in English, and the three most common letters in the ciphertext message were D, X and B, it would be worth trying to substitute those with E, T and A.

There are ways to frustrate a codebreaker attempting to use frequency analysis to decipher a message. One is to use a letter within the plaintext message, before it is enciphered, to indicate a break between words (X is often chosen). So the plaintext message


```
 PLEASE SEND ME A NEW CODE BOOK

```

would be transformed into


```
 PLEASEXSENDXMEXAXNEWXCODEXBOOK

```

before being enciphered, meaning that X appears in the message much more frequently than would be expected (in the example it is now the most frequent letter). 

If the distribution of letters within a ciphertext does not look like those within a natural language (where a few more common letters are likely to make up a significant amount of the text, and some letters may appear rarely or not at all), then it is likely that the ciphertext has not been encoded using a monoalphabetic cipher at all, and frequency analysis will not help you break it.
