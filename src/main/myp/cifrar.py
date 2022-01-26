# Utilizamos getpass para solicitar al usuario una contraseña sin hacer eco.
import getpass
# Utilizamos hashlib para implementar SHA-256.
import hashlib
# Utilizamos AES para cifrar los archivos solicitados.
from Cryptodome.Cipher import AES

from evalua import Evalua
   
class Cifrar:      

    def getCifrado(nombre, n, t, claro):
        """
        Solicita una contraseña al usario para cifrar el texto claro.
        Llama a los metodos que obtienen el archivo con las evaluaciones 
        del polinomio y el archivo con el texto cifrado.
        
        Parametros:
        nombre -- el nombre del archivo con las n evaluaciones.
        n -- las evaluaciones requeridas.
        t -- el mínimo número de participantes.
        claro -- el archivo con el texto a cifrar.
        """              
        k_sha = Cifrar.sha(getpass.getpass("Contraseña: "))
        k = int.from_bytes(k_sha, 'big')

        Cifrar.getEvArch(nombre, n, t, k)
        Cifrar.getArchC(claro, k_sha)

    def sha(cont):
        """
        Devuelve la dispersión de 256 bytes de la contraseña 
        introducida por el usuario.

        Parametros:
        cont -- la contraseña a dispersar.
        """
        return hashlib.sha256(cont.encode('utf-8')).digest()

    def getEvArch(nombre, n, t, k):
        """
        Obtiene el archivo con las 'n' evaluaciones 
        llamando al método que las obtiene con el 
        algoritmo de SSS.

        Guarda las evaluaciones en un documento con el 
        nombre indicado en los parámetros y extensión (.frg).

        Parametros:
        nombre -- el nombre con el que se guardará el archivo de evaluaciones.
        n -- el número de evaluaciones a realizar.
        t -- el mínimo número de fragmentos a aceptar.
        k -- la llave en que se ocultará con SSS.
        """
        parejas = Evalua.toString(Evalua.getEvaluaciones(n,t,k))
        if "." not in nombre: 
            nombre += ".frg" 
        else:
            nombre = "".join(nombre.split(".")[0:-1]) + ".frg"       
        archivo = open(nombre,"w")
        archivo.writelines(parejas)
        archivo.close()
        print("Se obtuvieron las evaluaciones en: " + nombre)

    def getArchC(claro, k_sha):
        """
        Obtiene un archivo de texto cifrado a partir del documento 
        claro proporcionado por el usuario, obtiene la información 
        a cifrar en bits y manda a llamar al método correspondiente
        para encriptar.
        
        Guarda el texto cifrado en un documento con extensión (.aes).

        Parametros:
        claro -- el archivo que se quiere cifrar.        
        k_sha -- la llave en bytes que se utilizará para cifrar.
        """
        with open(claro, 'rb') as fo:
            texto = fo.read()
        texto_cif = Cifrar.getEncriptado(texto, k_sha)
        claro += ".aes"
        with open(claro, 'wb') as fo:
            fo.write(texto_cif)
        print("Archivo cifrado exitosamente en: " + claro)         
    
    def getEncriptado(texto, llave):
        """
        Genera una versión cifrada de un texto a través de 
        un mecanismo de cifrado simétrico (AES), que admite 
        claves de cifrado de 256 bits.
        
        Parametros:
        texto -- el texto en bytes que se busca cifrar.        
        llave -- la llave en bytes que se utilizará para cifrar.
        """
        cifrado_aes = AES.new(llave, AES.MODE_EAX)
        t_cif, etiqueta = cifrado_aes.encrypt_and_digest(texto)
        return cifrado_aes.nonce + etiqueta + t_cif        