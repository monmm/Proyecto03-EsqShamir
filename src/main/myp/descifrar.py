from decimal import *
from binascii import unhexlify
from Crypto.Cipher import AES
#from Crypto.Protocol.SecretSharing import Shamir

class Descifrar:
    
    def llamaDecifrar(arr):
        """
        Llama al metodo correspondiente para descifrar y 
        guarda el mensaje descifrado con el nombre original.
        
        Parametros:
        arr -- la entrada con los argumentos recibidos
        """
       # mensaje_dev = Develar.devela(arr[0])
        des = arr[1]
        if "." not in des: 
            des += ".txt" 
        else:
            des = "".join(arr[1].split(".")[0:-1]) + ".txt"
        arch_des = open(des, "w")             
       # arch_des.write(mensaje_dev)
        arch_des.close()
        print ("Mensaje obtenido en: ", des)

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
    
    """
    def descifra():
        shares = []
        for x in range(2):
            in_str = raw_input("Enter index and share separated by comma: ")
            idx, share = [ strip(s) for s in in_str.split(",") ]
            shares.append((idx, unhexlify(share)))
        key = Shamir.combine(shares)

        with open("enc.txt", "rb") as fi:
            nonce, tag = [ fi.read(16) for x in range(2) ]
            cipher = AES.new(key, AES.MODE_EAX, nonce)
        try:
            result = cipher.decrypt(fi.read())
            cipher.verify(tag)
            with open("clear2.txt", "wb") as fo:
                fo.write(result)
        except ValueError:
            print ("The shares were incorrect")
    """

    def decrypt(key, data):
        nonce = data[:AES.block_size]
        tag = data[AES.block_size:AES.block_size * 2]
        ciphertext = data[AES.block_size * 2:]

        cipher = AES.new(key, AES.MODE_EAX, nonce)
    
        return cipher.decrypt_and_verify(ciphertext, tag)
