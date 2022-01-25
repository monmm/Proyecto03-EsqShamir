import getpass
import hashlib
from Cryptodome.Cipher import AES

from evalua import Evalua
   
class Cifrar:      

    def getCifrado(nombre, n, t, claro):
        """
        Solicita una contraseña al usario para cifrar el texto claro.
        Llama a los metodos que obtiene el archivo con las evaluaciones 
        del polinomio y el archivo con el texto cifrado.
        
        Parametros:
        nombre -- el nombre del archivo con las n evaluaciones.
        n -- las evaluaciones requeridas.
        t -- el mínimo número de participantes.
        claro -- el archivo con el texto a cifrar.
        """
        # Obtener la clave para cifrar
        pswd = getpass.getpass("Contraseña: ")
        k_sha = hashlib.sha256(pswd.encode('utf-8')).digest()
        k = int.from_bytes(k_sha, 'big')
        
        # Generamos el archivo con las evaluaciones del polinomio      
        Cifrar.getEvArch(nombre, n, t, k)

        # Generamos el archivo cifrado
        Cifrar.getArchC(claro, k_sha)

    def getEvArch(nombre, n, t, k):
        # Crear las evaluaciones del polinomio
        ev = Evalua.toString(Evalua.getEvaluaciones(n,t,k))
        if "." not in nombre: 
            nombre += ".frg" 
        else:
            nombre = "".join(nombre.split(".")[0:-1]) + ".frg"       
        archivo = open(nombre,"w")
        archivo.writelines(ev)
        archivo.close()

    def getArchC(claro, k_sha):
        with open(claro, 'rb') as fo:
            plaintext = fo.read()
        texto_cif = Cifrar.getEncriptado(plaintext, k_sha)

        if "." not in claro: 
            claro += ".frg" 
        else:
            claro = "".join(claro.split(".")[0:-1]) + ".aes"
        with open(claro, 'wb') as fo:
            fo.write(texto_cif)                    
    
    def getEncriptado(datos, llave):
        cipher = AES.new(llave, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(datos)
        return cipher.nonce + tag + ciphertext        