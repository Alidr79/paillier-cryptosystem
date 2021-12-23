class Paillier():    
    '''
    Paillier cryptosystem as an scheme of Homomorphic Encryption.
    By Ali_Derakhshesh
    Contact : ali.derakhshesh79@gmail.com
    
    It can perform addition on ciphertexts.
    p , q : two prime numbers
    'for better performance always use large prime numbers.'
    
    max_z_space_len : the maximum numbers to find in the Z* space
    by default is 100
    
    fast : by default is True
    Note : if fast == True, because of the random number we may face to  
    'not invertible' error but the code runs faster.
    if fast == False, the code is slower(may face to infinite loop)
    but the chance to face 'not invertible' error is lower.
    
    If the gcd(x , module) == 1 then we dont face to 'not invertible' error.
    '''
        
    # prime numbers
    __p = None
    __q = None
    
    # public key set
    __n = None
    __g = None
    
    # private key set
    __lambda = None
    __mu = None
    
    
    
    def __init__(self , p  , q , max_z_space_len = 100 , fast = True):
        
        import random
        
        # 1.chek for prime
        if ((not self.__is_prime(p)) or (not self.__is_prime(q))):
            raise ValueError('Error in initializing...\n            p and q must be prime!')
        
        n = (p*q)
        phi = (p-1)*(q-1)
        
        # 2. chek for indepently
        # for ex. p = 3 , q = 7 then p*q and (p-1)*(q-1) are dependent
        if self.__GCD(n , phi) != 1:
            raise ValueError('Error in initializing...\n            p*q and (p-1)*(q-1) are not independent!')
        
        
        self.__p = p
        self.__q = q
        self.__n = n
        self.__lambda = self.__LCM((self.__p - 1) , (self.__q - 1))
        
        
        zStar_space = self.__zStar_space(self.__n , max_z_space_len)
        
        if fast:
            self.__g = random.choice(zStar_space)
            helper_mu = self.__L( pow(self.__g , self.__lambda , (self.__n**2) ) , self.__n)
        
        else :
            while True:
                self.__g = random.choice(zStar_space)
                helper_mu = self.__L( pow(self.__g , self.__lambda , (self.__n**2) ) , self.__n)
                if self.__GCD(helper_mu , self.__n) == 1:
                    break
                    
                    
        # some cases are not invertible !!! like when x = 4 and module = 2
        # But what is the cause? because of common factors between number and module
        # If the gcd(x , module) == 1 then we dont face this problem.
        self.__mu = self.__modular_multiplicative_inverse(helper_mu , self.__n)
    
    
    
    def add_cipher(self , cipher1 , cipher2):
        '''
        Add two given ciphertexts and return the cipher result.
        '''
        return (cipher1 * cipher2) % (self.__n**2)    
    
    def get_public_key(self):
        '''
        Return the public key set {n , g}.
        '''
        return self.__n , self.__g

    def get_private_key():
        '''
        Return the private key set {lambda , mu}.
        '''
        return self.__lambda , self.__mu
    
    def encrypt(self , message):
        '''
        Encrypt plaintext, using the public key ,into ciphertext.
        '''
        import random
        
        r = random.randint(0,(self.__n - 1))
        ciphertext = (self.__g**message)*(r**self.__n)
        ciphertext %= (self.__n**2)
        
        return ciphertext
    
    def decrypt(self , ciphertext):
        '''
        Decrypt ciphertext, using the private key ,into plaintext.
        '''
        
        helper = ((ciphertext**self.__lambda)%(self.__n**2))      
        helper = self.__L(helper , self.__n)
        plaintext = (helper*self.__mu)%self.__n
        
        return plaintext
        
    def __modular_multiplicative_inverse(self , x , module):
        return pow(x , -1 , module)
        
    def __is_prime(self , x):
        
        # Return True if the given number is prime,otherwise return False.
        
        for i in range(2,x):
            if (x%i) == 0:
                return False
        return True
    
    def __zStar_space(self , n , max_z_space_len):
        
        
#         Return The z* space.
#         In number theory, Zn is the set of non-negative integers less than n ({0,1,2,3...n-1}).
#         z* (z* modulo n) is then a subnet of this which is the multiplicative group for Zn modulo n.
#         The set z* is the set of integers between 1 and n that are relatively prime to n (ie they do not share any factors).
        
        n_2 = n**2
        
        _zStar = []
        for i in range(1 , n_2):
            if self.__GCD(n_2 , i) == 1:
                _zStar.append(i)
                
            # avoid large values because of time cost
            if len(_zStar) == max_z_space_len:
                break
            
        return _zStar
            
    def __GCD(self , a , b):
        # Return the greates common divisor of a and b
        
        gcd = 1
    
        if b<a:
            a , b = b , a
        for i in range(1,a+1):
            if (b%i == 0) and (a%i == 0):
                gcd = i
    
        return gcd
    
    
    def __LCM(self , a , b):

        # Return the least common multiplier of a and b
        
        if b > a:
            a , b = b , a
    
        for i in range(a , (a*b)+1):
            if (i%a == 0) and (i%b == 0):
                return i
        
    def __L(self , x , n):
        return ((x-1)//n)