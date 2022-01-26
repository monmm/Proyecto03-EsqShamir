# Utilizamos AES para descifrar los archivos solicitados.
from Cryptodome.Cipher import AES

class Descifrar:
    
    def getDescifrado(min_ev, cifrado):
        """
        Llama al metodo correspondiente para descifrar y 
        guarda el mensaje descifrado con el nombre del 
        texto original.
        
        Parametros:
        min_ev -- las evaluaciones del polinomio, al menos t.
        cifrado -- el archivo de texto cifrado.
        """                    
        if "." not in min_ev: 
            min_ev += ".frg" 
        else:
            min_ev = "".join(min_ev.split(".")[0:-1]) + ".frg"
        ev = Descifrar.getPares(min_ev)    
        k = Descifrar.getLlave(ev)
        Descifrar.getArchD(cifrado, k.to_bytes(32, 'big'))                

    def getPares(min_ev):
        """
        Obtiene una lista con las evaluaciones del polinomio 
        proporcionadas por el usuario.

        Parametros:
        min_ev -- el archivo con las evaluaciones.
        """
        evaluaciones = []
        fragmentos = []
        archivo = open(min_ev, "r")        
        evaluaciones = archivo.readlines()        
        evaluaciones = [el.strip('\n') for el in evaluaciones]        
        evaluaciones = [tup.strip('()') for tup in evaluaciones]        
        for par in evaluaciones:            
            fragmentos.append(tuple(map(int, par.split(', '))))
        return fragmentos    

    def getLlave(puntos):
        """
        Utilizamos el polinomio de Lagrange para nuestra interpolación, 
        obteniendo el punto de grado más bajo, que usaremos como llave 
        para desencriptar.

        Parametros:
        puntos -- las evaluaciones de los puntos en el plano.
        """
        primo = 2**521 - 1
        p_cero = 0
        x = 0

        for i in range(len(puntos)):
            xi, yi = puntos[i]
            p_cero = (primo + p_cero + Descifrar.getPolinomio(puntos, xi, x, i, yi, primo)) % primo

        return p_cero

    def getPolinomio(puntos, xi, x, i, yi, primo):
        """
        Calculamos el polinomio de interpolación de Lagrange en xi,
        obteniendo el inverso multiplicativo del denominador.
        
        Parametros:
        puntos -- las evaluaciones de los puntos en el plano.
        xi -- el punto de interpolación del polinomio.
        i -- el indice
        yi -- la función aplicada del punto xi
        primo -- el número primo utilizado para el modulo.
        """
        polinomio = []

        for j in range(len(puntos)):
            if (j == i):
                continue

            num = (x - puntos[j][0]) % primo
            denom = (xi - puntos[j][0]) % primo
            inverso = pow(denom, primo-2, primo)            
            polinomio.append(num * inverso)

        result = 1
        for k in range(len(polinomio)):
            result *= polinomio[k]

        return result * yi

    def getArchD(cifrado, llave):
        """
        Obtiene el archivo de texto original a partir un documento 
        cifrado proporcionado por el usuario, obtiene la información 
        a descifrar en bits y manda a llamar al método correspondiente
        para desencriptar.
        
        Guarda el texto descifrado en el documento con el mismo nombre 
        que el archivo original.

        Parametros:
        cifrado -- el archivo que se quiere descifrar.        
        llave -- la llave en bytes que se utilizará para descifrar.
        """
        with open(cifrado, 'rb') as fo:
            t_des = fo.read()
        desencript = Descifrar.getDesencriptado(llave, t_des)        
        with open(cifrado[:-4], 'wb') as fo:
            fo.write(desencript)        
        print ("Archivo descifrado exitosamente en: ", cifrado[:-4])
    
    def getDesencriptado(llave, datos):
        """
        Obtiene la versión original de un archivo de texto a 
        través de un proceso de descifrado con AES, que admite 
        claves de cifrado de 256 bits.
        
        Parametros:
        llave -- la llave en bytes que se utilizará para cifrar.
        datos -- el texto en bytes que se busca descifrar.          
        """
        nonce = datos[:AES.block_size]
        etiqueta = datos[AES.block_size:AES.block_size * 2]
        t_des = datos[AES.block_size * 2:]

        cipher = AES.new(llave, AES.MODE_EAX, nonce)
        return cipher.decrypt_and_verify(t_des, etiqueta)    