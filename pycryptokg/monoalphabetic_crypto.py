import random
import math

class MonoalphabeticCrypto:
    default_key1 = None
    default_key2 = None
    def __init__(self):
        self.default_key1 = random.randint(1,1000000)
        self.default_key2 = random.randint(1,1000000)
        
    def gcd(self, a, b):
        if b==0:
            return a
        return self.gcd(b,a%b)
    
    def multiplicative_inverse(self, key, N):
        if self.gcd(N, key)!=1:
            return None
        m0 = N
        y = 0
        x = 1
        if N == 1: 
            return 0
    
        while key > 1: 
            # q is quotient 
            q = key // N 
            t = N
            # m is remainder now, process 
            # same as Euclid's algo 
            N = key % N 
            key = t 
            t = y 
            # Update x and y 
            y = x - q * y 
            x = t 
            
        # Make x positive 
        if (x < 0) : 
            x = x + m0 
        return x
    
    def additive_cipher_encrypt(self, plain_text, key = default_key1 , N = 95):
        cipher_text = []
        for ch in plain_text:
            cipher_ch=chr((ord(ch) - 32 + key)%N + 32)
            cipher_text.append(cipher_ch)
        return "".join(cipher_text)
    
    def additive_cipher_decrypt(self, cipher_text, key = default_key1, N = 95):
        plain_text = []
        for ch in cipher_text:
            plain_ch=chr((ord(ch) - 32 - key)%N + 32)
            plain_text.append(plain_ch)
        return "".join(plain_text)
    
    def multiplicative_cipher_encrypt(self, plain_text, key = default_key1, N = 95):
        key_inv = self.multiplicative_inverse(key, N)
        if key_inv==None:
            print "Supplied Key doesn't have a multiplicative inverse"
            return
        cipher_text = []
        for ch in plain_text:
            cipher_ch = chr( ((ord(ch)-32)*key)%N + 32 )
            cipher_text.append(cipher_ch)
            
        
        return key_inv, "".join(cipher_text)
    
    def multiplicative_cipher_decrypt(self, cipher_text, key, N = 95):
        plain_text = []
        for ch in cipher_text:
            plain_ch=chr(( (ord(ch) - 32)*key)%N + 32)
            plain_text.append(plain_ch)
        return "".join(plain_text)
    
    def affine_cipher_encrypt(self, plain_text, key1 = default_key1, key2 = default_key2, N = 95):
        keyinv1, cipher_text1 = self.multiplicative_cipher_encrypt(plain_text, key1)
        if keyinv1==None:
            return
        cipher_text2 = self.additive_cipher_encrypt(cipher_text1, key2)
        return keyinv1, cipher_text2
        
    def affine_cipher_decrypt(self, cipher_text, key1, key2 = default_key1, N = 95):
        plain_text1 = self.additive_cipher_decrypt(cipher_text, key2)
        plain_text2 = self.multiplicative_cipher_decrypt(plain_text1, key1)
        return plain_text2
    
        
        
    
