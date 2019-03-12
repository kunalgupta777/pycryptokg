from __future__ import print_function
import random, math, numpy

class PolyalphabeticCrypto:
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
    
    def get_key_matrix(self, key):
        l = int(math.sqrt(len(key)))
        key_matrix = []
        i = 0
        block = []
        for ch in key:
            if i==l:
                i = 0
                key_matrix.append(block)
                block = []

            block.append(ord(ch)-32)
            i+=1
        key_matrix.append(block)
        return key_matrix
                
    
    def check_key(self, key, N):
        l = math.sqrt(len(key))
        if l-int(l)!=0:
            return False
        
        key_matrix = self.get_key_matrix(key)
        det = numpy.linalg.det(key_matrix)
        if det==0:
            return False
        inv = self.multiplicative_inverse(det, N)
        if inv==None:
            return False
        return True
        
        
        
    def generate_hill_key(self, N):
        n = random.randint(2,5)
        l = n*n
        while True:
            key = [chr(random.randint(32, 127)) for _ in range(l)]
            if self.check_key(key, N)==True:
                break
        return "".join(key)
        
        
    def generate_playfair_key(self):
        key_dict = {}
        key = [[None for i in range(10)] for j in range(10)]
        check = {chr(i):False for i in range(32,133)}
        for i in range(10):
            for j in range(10):
                while True:
                    ch = chr(random.randint(32,132))
                    if check[ch]==False:
                        key_dict[ch] = (i,j)
                        key[i][j] = ch
                        check[ch] = True
                        break
        return key, key_dict
                    
        
    
    def autokey_cipher_encrypt(self, plain_text, key = default_key1, N = 95 ):
        cipher_text = []
        key_created = [key]
        for i in range(len(plain_text)):
            cipher_text.append( chr((ord(plain_text[i]) - 32 + key)%N + 32) )
            key = ord(plain_text[i])
            key_created.append(key)
        return key_created, "".join(cipher_text)
        
    def autokey_cipher_decrypt(self, cipher_text, key, N = 95):
        plain_text = []
        for i in range(len(cipher_text)):
            plain_text.append(chr((ord(cipher_text[i])-32-key[i])%N+32))
        return "".join(plain_text)
    
    def playfair_cipher_encrypt(self, plain_text, key = None, key_dict = None):
        if key==None:
            key, key_dict = self.generate_playfair_key()
        elif key_dict==None:
            key_dict = {}
            for i in range(10):
                for j in range(10):
                    key_dict[key[i][j]] = (i,j)
            
        cipher_text = []
        pair_list = []
        i = 0
        while i<len(plain_text):
            if i+1==len(plain_text):
                pair_list.append((plain_text[i],'$'))
                break
            elif plain_text[i]==plain_text[i+1]:
                pair_list.append((plain_text[i],'$'))
                i+=1
            else:
                pair_list.append((plain_text[i], plain_text[i+1]))
                i+=2
        
        for pair in pair_list:
            c1 = pair[0]
            c2 = pair[1]
            c1r, c1c = key_dict[c1]
            c2r, c2c = key_dict[c2]
            
            if c1r==c2r:
                cipher_text.append(key[c1r][(c1c+1)%10])
                cipher_text.append(key[c2r][(c2c+1)%10])
            elif c1c==c2c:
                cipher_text.append(key[(c1r+1)%10][c1c])
                cipher_text.append(key[(c2r+1)%10][c2c])
            else:
                cipher_text.append(key[c1r][c2c])
                cipher_text.append(key[c2r][c1c])
        return key, key_dict, "".join(cipher_text)
            
            
        
    def playfair_cipher_decrypt(self, cipher_text, key, key_dict):
        plain_text = []
        pair_list = []
        i = 0
        while i<len(cipher_text)-1:
            pair_list.append((cipher_text[i],cipher_text[i+1]))
            i+=2
        
        for pair in pair_list:
            c1 = pair[0]
            c2 = pair[1]
            c1r, c1c = key_dict[c1]
            c2r, c2c = key_dict[c2]
            
            if c1r==c2r:
                plain_text.append(key[c1r][(c1c-1)%10])
                plain_text.append(key[c2r][(c2c-1)%10])
            elif c1c==c2c:
                plain_text.append(key[(c1r-1)%10][c1c])
                plain_text.append(key[(c2r-1)%10][c2c])
            else:
                plain_text.append(key[c1r][c2c])
                plain_text.append(key[c2r][c1c])
        plain_text = [ plain_text[i]  for i in range(len(plain_text)) if plain_text[i]!='$' ]
        return "".join(plain_text)
    
    def vignere_cipher_encrypt(self, plain_text, key, N = 95):
        l = len(key)
        cipher_text = []
        i = 0
        for ch in plain_text:
            if i==l:
                i = 0
            cipher_text.append(chr((ord(ch) - 32 + ord(key[i])-32)%N + 32))
            i+=1
        return "".join(cipher_text)
        
            
    def vignere_cipher_decrypt(self, cipher_text, key, N = 95):
        l = len(key)
        plain_text = []
        i = 0
        for ch in cipher_text:
            if i==l:
                i= 0
            plain_text.append(chr( ( (ord(ch)-32) - (ord(key[i])-32) )%N +32))
            i+=1
        return "".join(plain_text)
    
    def hill_cipher_util(self, block, key_matrix, N):
        original_length = len(block)
        block = [ord(block[i])-32 for i in range(len(block))]
        if len(block) < len(key_matrix):
            block+= [0]*(len(key_matrix)-len(block))
        
        res = numpy.dot(block, key_matrix)
        res = res%N + 32
        res = numpy.array(res).tolist()
        return [chr(res[i]) for i in range(original_length)]
    
    
        
        
    def hill_cipher_encrypt(self, plain_text, key = None , N = 95):
        if key == None:
            key = self.generate_hill_key(N)
        elif self.check_key(key, N)==False:
                print("Key is Not compatible for decryption!")
                return
                
        
        l = int(math.sqrt(len(key)))
        key_matrix = self.get_key_matrix(key)
        blocks = []
        i = 0
        block = []
        for ch in plain_text:
            if i==l:
                blocks.append(block)
                block = []
                i = 0
            block.append(ch)
            i+=1

        blocks.append(block)
                
        #blocks prepared
        cipher_blocks = []
        for block in blocks:
            cipher_blocks.append(self.hill_cipher_util(block, key_matrix, N))
                
        cipher_text = []
        for cipher_block in cipher_blocks:
            cipher_text.append("".join(cipher_block))
        
        return key, "".join(cipher_text)
                        
                    
    def get_inverse(self, key_matrix, N):
        det = numpy.linalg.det(key_matrix)
        detinv = self.multiplicative_inverse(det, N)
        
        key_matrix = numpy.linalg.inv(key_matrix)
        key_matrix = (key_matrix*det)%N
        key_matrix = (key_matrix*detinv)%N
        return numpy.array((key_matrix).astype(int)).tolist()
        
            
    def hill_cipher_decrypt(self, cipher_text, key, N = 95):
        if self.check_key(key, N)==False:
            print("Invalid Key!")
            return 
        l = int(math.sqrt(len(key)))
        key_matrix = self.get_key_matrix(key)
        blocks = []
        i = 0
        block = []
        for ch in cipher_text:
            if i==l:
                blocks.append(block)
                block = []
                i = 0
            block.append(ch)
            i+=1

        blocks.append(block)
                
        #blocks prepared
        
        # inverting the key matrix
        key_matrix = self.get_inverse(key_matrix, N)
        # P = C*K_inv
        plain_blocks = []
        
        for block in blocks:
            plain_blocks.append(self.hill_cipher_util(block, key_matrix, N))
                
        plain_text = []
        for plain_block in plain_blocks:
            plain_text.append("".join(plain_block))
        
        return "".join(plain_text)
