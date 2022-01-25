import getpass
import hashlib
import random 
from functools import reduce
from operator import mul
from mod import Mod
from Cryptodome.Cipher import AES
from math import ceil 
from decimal import *
import secrets
   
      
global field_size 
field_size = 10**5
   
def reconstructSecret(shares):           
    
    sums, prod_arr = 0, [] 
      
    for j in range(len(shares)): 
        xj, yj = shares[j][0],shares[j][1] 
        prod = Decimal(1) 
          
        for i in range(len(shares)): 
            xi = shares[i][0] 
            if i != j: prod *= Decimal(Decimal(xi)/(xi-xj)) 
                  
        prod *= yj 
        sums += Decimal(prod) 
          
    return int(round(Decimal(sums),0)) 
   
def polynom(x,coeff):       
            
    return sum([x**(len(coeff)-i-1) * coeff[i] for i in range(len(coeff))]) 
   
def coeff(t,secret): 
                  
    coeff = [random.randrange(0, field_size) for _ in range(t-1)] 
    coeff.append(secret) 
      
    return coeff 
   
def generateShares(n,m,secret): 
      
    cfs = coeff(m,secret) 
    shares = [] 
      
    for i in range(1,n+1): 
        r = random.randrange(1, field_size) 
        shares.append((r, polynom(r,cfs))) 
      
    return shares 
  
def imprime(shares):

    for i in shares:
        print(i)

def encrypt(key, data):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    return cipher.nonce + tag + ciphertext

def retrieve_original(secrets):
    P = 2**521 - 1
    x_s = [s[0] for s in secrets]
    acc = Mod(0, P)
    for i in range(len(secrets)):
        others = list(x_s)
        cur = others.pop(i)
        factor = Mod(1, P)
        for el in others:
            factor *= el * (el - cur).inverse()
        acc += factor * secrets[i][1]
    return acc
  
if __name__ == '__main__': 
      
    
    t = 3
    n = 5
    pswd = getpass.getpass("Contraseña: ")
    k = hashlib.sha256(pswd.encode('utf-8')).digest()    
    secret = int.from_bytes(k, 'big')
    print('Original Secret:', secret) 
    print(len("{0:b}".format(secret)))    
    shares = generateShares(n, t, secret) 
    print('\nShares: \n')
    imprime(shares) 
   
    my_str = "hello world"
    #my_str_as_bytes = str.encode(my_str)
    encrypt(k, b'my_str_as_bytes')
    
    
    pool = random.sample(shares, t) 
    print('\nCombining shares:', *pool) 
    print("Reconstructed secret:", reconstructSecret(pool)) 
    