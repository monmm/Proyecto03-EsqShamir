import getpass
import hashlib
from Crypto.Cipher import AES
   
class Cifrar:      

    def getCifrado(nombre, n, t, claro):
        """
        Solicita una contraseña al usario para cifrar el texto claro.
        Obtiene el texto claro del archivo correspondiente y
        llama al metodo para cifrar con las evaluaciones y 
        valores correspondientes.
        
        Parametros:
        nombre -- el nombre del archivo con las n evaluaciones.
        n -- las evaluaciones requeridas.
        t -- el mínimo número de participantes.
        claro -- el archivo con el texto a cifrar.
        """
        # Obtener la clave para cifrar
        pswd = getpass.getpass("Contraseña: ")
        k = int.from_bytes(hashlib.sha256(pswd.encode('utf-8')).digest(), 'big')

        Cifrar.getEvArch(nombre, n, t, k)        
        with open(claro, 'rb') as fo:
            plaintext = fo.read()
            Cifrar.getEncriptado
                
    def getEvArch(nombre, n, t, k):
        # Crear las evaluaciones del polinomio
        ev = Cifrar.toString(Cifrar.getEvaluaciones(n,t,k))
        if "." not in nombre: 
            nombre += ".frg" 
        else:
            nombre = "".join(nombre.split(".")[0:-1]) + ".frg"       
        archivo = open(nombre,"w")
        archivo.writelines(ev)
        archivo.close()
    
    def getEncriptado(llave, datos):
        cipher = AES.new(llave, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(datos)
        return cipher.nonce + tag + ciphertext    