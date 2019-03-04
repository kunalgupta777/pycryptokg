# pycryptokg
A cryptography library for Python 2.7.
Here's a broad description of the cryptography techniques given
## Symmetric Key  Cryptography Techniques ##
 - [x] 1 **Substitution ( each character is substituted with another, can be a different space than the plaintext )**
 
   - [x] 1.1 Monalphabetic ( every character is substituted to the same character, no matter the position )
     - [x] 1.1.1 Additive Cipher ( aka Shift, Caesar )
     - [x] 1.1.2 Multiplicative Cipher
     - [x] 1.1.3 Affine Cipher
     
   - [x] 1.2 Polyalphabetic Cipher ( the value of the substituted character depends on both its value and it's position )
     - [x] 1.2.1 Autokey Cipher
     - [x] 1.2.2 Playfair Cipher
     - [x] 1.2.3 Vignere Cipher
     - [x] 1.2.4 Hill Cipher
     
 - [ ] 2 **Transpostion ( The orders of the characters is interchanged )**
     - [ ] 2.1 Keyless Transposition
     - [ ] 2.2 Keyed Transposition
   
 - [ ] 3 **Modern Symmetric Ciphers**
     - [ ] 3.1 Data Encryption Standard ( DES )
     - [ ] 3.2 Advanced Encryption Standard ( AES )
   
## Asymmetric Key (Public Key) Cryptography Techniques ##
 - [x] 1. Rivest, Shamir, Adleman ( RSA ) Cryptosystem
 - [ ] 2. Rabin Cryptosystem
 - [x] 3. Merkle-Hellman Knapsack Cryptosystem
 - [ ] 4. El-Gamal Cryptosystem
 - [ ] 5. Elliptic Curve Cryptosystem
 
## How to use?
Open a terminal and use
 ``` 
 pip install cryptopy
 ```
 You can use
 ```
 help(cryptopy) 
 ```
 for documentation about the API's
