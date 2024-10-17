
# The Vigenère Cipher (Brian Hicks)

From the Quicksilver Metaweb.

The Vigenère cipher is a cipher which can be considered the superset of most modern [stream ciphers](/stream-cipher). Basically, a key is used to generate a keystream, which is then combined with the [plaintext](/plaintext) to yield a [ciphertext](/ciphertext). The keystream itself is a function of the key which is the length of the plaintext, in the case of the textbook Vigenère cipher the keystream is simply the key repeated to the length of the plaintext. For the [one-time pad](/one-time-pad) the keystream is exactly equal to a randomly-generated key the length of the plaintext. There are also autokey stream ciphers, in which the keystream is a function of both the key and the preceeding section of the plaintext.

The combination of the keystream with the plaintext was classically achieved by generating a *tabula recta*, a square with the alphabet written horizontally along the top and vertically along the left side, and the inner space filled by 25 alphabets shifted to start with the letter along the left side. A slightly simpler method had the alphabet written along the top and the keyword written along the left, with the alphabets inside starting off the various letters of the key. For both these methods, the column starting with the plaintext letter to be encrypted was chosen, as was the row starting with the corresponding keystream letter. The intersection of these lines was the ciphertext.

A more general form of this combination is convert the letters into base-26 numbers. You can then perform [modulo](/modulo) 26 addition of the plaintext and keystream, and then convert the resulting number into a letter to get the ciphertext character. Some versions of the cipher treat A as 0, while others treat A as 1 with Z being 0 (0 being 26 modulo 26).

Of course, the only significance of modulo 26 addition is that there are 26 symbols (letters), you could easily add other symbols, such as the ampersand, and use modulo 27 or higher addition. Conversely, you could just as easily turn all of the Js into Is and perform modulo 25 addition, as was done by [Lawrence Waterhouse](/stephenson-neal-cryptonomicon-lawrence-waterhouse) in [Cryptonomicon](/stephenson-neal-cryptonomicon).

Even more common, with the advent of computers, you could convert all of your information into binary form and perform modulo 2 addition to encrypt. Conveniently, modulo 2 addition gives the same result as modulo 2 subtraction, referred to as a logical XOR. By using a XOR function, you can decrypt a ciphertext with the exact same method used to encrypt the plaintext.
