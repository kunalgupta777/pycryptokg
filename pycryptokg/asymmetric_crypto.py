from __future__ import print_function
import math, random

class AsymmetricCrypto:
    def __init__(self):
        pass
    
    def gcd(self, a, b):
        if b==0:
            return a
        return self.gcd(b,a%b)
    
    def isPrime(self, n):
        if n==2:
            return True
        if n%2==0:
            return False
        i = 3
        while i*i<=n:
            if n%i==0:
                return False
            i+=2
        return True
    
    def generate_large_prime(self):
        while True:
            p = random.randint(10001,1000001)
            if self.isPrime(p)==True:
                return p
    
    def rsa_generate_public_key(self):
        p = self.generate_large_prime()
        q = self.generate_large_prime()
        
        n = p*q
        phi = (p-1)*(q-1)
        
        e = None
        while True:
            e = random.randint(2,phi-1)
            if self.gcd(e,phi)==1:
                break
                
        return (n, e, p, q)
    
    def get_num_list(self, plaintext):
        return [ord(ch) for ch in plaintext ]
            
    def rsa_util_encrypt(self, num, public_key):
        n = public_key[0]
        e = public_key[1]
        
        return pow(num, e, n)
    
    def rsa_encrypt(self, plaintext, public_key=None):
        if public_key==None:
            public_key = self.rsa_generate_public_key()
        
        num_list = self.get_num_list(plaintext)
        cipher_nums = []
        for num in num_list:
            cipher_num = self.rsa_util_encrypt(num, public_key)
            cipher_nums.append(cipher_num)
        
        return public_key, cipher_nums
    
        
    def rsa_util_decrypt(self, cipher_num, private_key, public_key):
        n = public_key[0]
        d = private_key
        return pow(cipher_num, d, n)
    
    def multiplicative_inverse(self, a, n):
        if self.gcd(a, n)!=1:
            return None
        r1 = n
        r2 = a
        p1 = 0
        p2 = 1
        while r1>1:
            q = r1//r2
            r = r1 - q*r2
            r1 = r2
            r2 = r
            
            p = p1 - q*p2
            p1 = p2
            p2 = p
        
        return p1%n
            

    def get_private_key(self, public_key):
        n = public_key[0]
        e = public_key[1]
        
        p = public_key[2]
        q = public_key[3]
        
        phi = (p-1)*(q-1)
        
        d = self.multiplicative_inverse(e, phi)
        return d
    
    def rsa_decrypt(self, cipher_nums, public_key=None, private_key=None):
        if public_key==None:
            return "Please Provide a public key!!"
        if private_key==None:
            return "Please Provide a private Key!!"
        
        plain_nums = []
        for cipher_num in cipher_nums:
            plain_num = self.rsa_util_decrypt(cipher_num, private_key, public_key)
            plain_nums.append(plain_num)
        plain_text = [ chr(plain_num) for plain_num in plain_nums ]
        
        return "".join(plain_text), plain_nums
    
    def knapsack_generate_keys(self, n=8):
    
        ## first create a superincreasing sequence of length 'n'
        seed = random.randint(2,10)
        super_sequence = [seed]

        for i in range(n-1):
            sum_so_far = sum(super_sequence)
            element = random.randint(sum_so_far+1, 2*sum_so_far)
            super_sequence.append(element)

        ## now select a random integer q such that q > sum(super_sequence)
        q = random.randint(sum(super_sequence)+1, 2*sum(super_sequence))

        ## now select another random integer 'r' such that gcd(q,r) = 1
        r = 2
        while True:
            r = random.randint(2,q-1)
            if self.gcd(q,r) == 1:
                break
        ## Finally, calculate beta - the public key

        beta = tuple( (r*super_sequence[i])%q for i in range(n) ) ## making beta as a tuple, as tuples are immutable 

        private_key = (super_sequence, q, r)

        return beta, private_key



    ##The below function finds alpha as a part of decryption
    def getalpha(self, c, w):
        w = w[::-1]
        alpha = []
        for number in w:
            if number > c:
                alpha.append(0)
            else:
                alpha.append(1)
                c = c - number
        return alpha[::-1]


    def knapsack_encrypt(self, plaintext, public_key):
        ciphertext = []
        for character in plaintext:
            binary = bin(ord(character))
            binary = binary[0]+binary[2:]
            l = len(binary)
            binary = (8-l)*"0"+binary
            binary = list(map(int,binary))
            # now, binary is an 8 element list, containing bits of binary representation of the character
            # ciphertext 'c' is calculated now
            c = sum([ binary[i]*public_key[i] for i in range(len(public_key)) ])
            ciphertext.append(c)
        return ciphertext

    def knapsack_decrypt(self, ciphertext, private_key):
        #First, we calculate the integer 's' , which has the property that:
        # r*s = 1 mod q
        #unpack private key
        super_sequence, q, r = private_key
        s = self.multiplicative_inverse(r, q)
        # finding c' = modified ciphertext
        modified_ciphertext = [ (ciphertext[i]*s)%q for i in range(len(ciphertext)) ]

        decrypted_text = []
        ## Now, for each modified ciphertext, we will find the actual alpha sequence 
        i = 0
        for c in modified_ciphertext:
            alpha = self.getalpha(c,super_sequence)
            alpha = "".join(map(str, alpha))
            decrypted_text.append(chr(int(alpha,2)))
            i+=1

        return "".join(decrypted_text)
    
    
        
            