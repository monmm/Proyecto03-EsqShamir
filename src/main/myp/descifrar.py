from decimal import *
from Cryptodome.Cipher import AES

class Descifrar:
    
    def getDescifrado(min_ev, cifrado):
        """
        Llama al metodo correspondiente para descifrar y 
        guarda el mensaje descifrado con el nombre original.
        
        Parametros:
        arr -- la entrada con los argumentos recibidos
        """            
        evaluaciones = []   
        if "." not in min_ev: 
            min_ev += ".frg" 
        else:
            min_ev = "".join(min_ev.split(".")[0:-1]) + ".frg"
        parejas = open(min_ev, "r")
        evaluaciones = parejas.readlines()
        Descifrar.reconstructSecret(evaluaciones)
        print ("Mensaje obtenido en: ", cifrado)

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

    def getDescencriptado(llave, datos):
        nonce = datos[:AES.block_size]
        tag = datos[AES.block_size:AES.block_size * 2]
        ciphertext = datos[AES.block_size * 2:]

        cipher = AES.new(llave, AES.MODE_EAX, nonce)
    
        return cipher.decrypt_and_verify(ciphertext, tag)

    def decrypt_file(file_name, key):
        with open(file_name, 'rb') as fo:
            ciphertext = fo.read()
        #dec = decrypt(ciphertext, key)
        with open(file_name[:-4], 'wb') as fo:
            fo.write("dec")