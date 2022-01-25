"""
Clase principal de nuestro programa, valida los argumentos de entrada 
y manda a llamar los métodos correspondientes según la opción indicada 
por las banderas de entrada con los argumentos recibidos.
"""
from cifrar import Cifrar
from descifrar import Descifrar

# Usamos sys para leer la entrada de terminal
import sys
# Usamos os para verificar la existencia de nuestros archivos
import os
# Usamos unidecode para simplicar el texto a ocultar
from unidecode import unidecode

class Shamir:

    def __init__(self):
        pass            

    def verifica():
        """
        Verifica que la entrada sea correcta.
        
        Que tenga las banderas adecuadas 
        - c para cifrar
        - d para decifrar
        y reciba los argumentos correspondientes.
        En caso contrario, imprime el modo de uso del programa.
        """
        if len(sys.argv) <= 1:        
            Shamir.imprimeUso("%s" % sys.argv[0])
        elif (sys.argv[1] == "c"):        
            if len(sys.argv) != 6:
                Shamir.imprimeUso("Se requieren 5 argumentos, usted introdujo %d" % (len(sys.argv) - 1))
            else:
                Shamir.verificaCifrar(sys.argv[2:6])        
        elif (sys.argv[1] == "d"):
            if len(sys.argv) != 4:
                Shamir.imprimeUso("Se requieren 3 argumentos, usted introdujo %d" % (len(sys.argv) - 1))
            else:
                Shamir.verificaDecifrar(sys.argv[2:4]);            
        elif (sys.argv[1] != "c" and sys.argv[1] != "d"):
            Shamir.imprimeUso("La entrada es incorrecta")

    def imprimeUso(mensaje):
        """
        Imprime cuáles son los argumentos que 
        se esperan recibir para que el programa funcione.
        
        Parametros:
        mensaje -- error de entrada capturado
        """
        print ("USO: " + mensaje)
        doc = "\n CIFRAR: \n - c nombre_guardar_n_ev num_ev_requeridas "        
        doc += "num_min_descifrar archivo_claro \n\n"
        doc += " Dónde el número de evaluaciones requeridas es n > 2 y \n"
        doc += " el mínimo número de evaluaciones a descifrar es​ 1 < t ≤ n ​\n\n"
        doc += " DECIFRAR: \n - d archivo_con_t_ev archivo_cifrado \n"
        sys.exit(doc)

    def verificaCifrar(arr):
        """
        Verifica que la entrada para cifrar sea correcta y 
        llama al metodo correspondiente para ello.
        
        Verifica que el archivo claro a cifrar exista, 
        en caso de que no, imprime el modo de uso.
        Asume que el metodo es destructivo y no verifica 
        si los nombres de destino ya existen.
        
        Parametros:
        arr -- la entrada con los argumentos recibidos
        Excepciones:
        SystemExit -- Si la entrada recibida no es válida
        """
        n = int(arr[1])
        t = int(arr[2])        
        if (n < 2):
            sys.exit("El número de evaluaciones requeridas es n > 2 ")        
        if (t > n or t < 2):
            sys.exit("El mínimo número de evaluaciones a descifrar es​ 1 < t ≤ n")                
        if not os.path.isfile(arr[3]):
            sys.exit("No se encontró el archivo de texto claro")            
        else:                      
            Cifrar.getCifrado(arr[0], n, t, arr[3])
        print("Nombre del archivo para guardar las evaluaciones " + arr[0])                
        print("Número de evaluaciones: " + arr[1])
        print("Número mínimo de evaluaciones: " + arr[2])
        print("El archivo claro es: " + arr[3])  
    
    def verificaDescifrar(arr):
        """
        Verifica que la entrada para decifrar sea correcta y 
        llama al metodo correspondiente para ello.
        
        Verifica que los archivos para decifrar existan, en caso 
        de que no, imprime el modo de uso.

        Parametros:
        arr -- la entrada con los argumentos recibidos
        Excepciones:
        SystemExit -- Si la imagen recibida no es válida
        """
        if not os.path.isfile(arr[0]):
            sys.exit("No se encontró el archivo con las evaluaciones")            
        else:
            print("El archivo con al menos t evaluaciones es: " + arr[0])
            #Descifrar.llamaDescifrar(arr[0], arr[1])     
        if not os.path.isfile(arr[1]):
            sys.exit("No se encontró el archivo de texto cifrado")            
        else:
            print("El archivo de texto cifrado es: " + arr[1])
            #Descifrar.llamaDescifrar(arr[0], arr[1])    

if __name__ == "__main__":
    Shamir.verifica()