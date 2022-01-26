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

class Shamir:

    def __init__(self):
        pass            

    def verifica():
        """
        Verifica que la entrada sea correcta.
        
        Que tenga las banderas adecuadas 
        - c para cifrar
        - d para descifrar
        y reciba los argumentos correspondientes.
        En caso contrario, imprime el modo de uso del programa.
        """
        if len(sys.argv) <= 1:        
            Shamir.imprimeUso("%s" % sys.argv[0])
        elif (sys.argv[1] == "c"):        
            if len(sys.argv) != 6:
                Shamir.imprimeUso("Se requieren 5 argumentos para cifrar, usted introdujo %d" % (len(sys.argv) - 1))
            else:
                Shamir.verificaCifrar(sys.argv[2:6])        
        elif (sys.argv[1] == "d"):
            if len(sys.argv) != 4:
                Shamir.imprimeUso("Se requieren 3 argumentos para descifrar, usted introdujo %d" % (len(sys.argv) - 1))
            else:
                Shamir.verificaDescifrar(sys.argv[2:4]);            
        elif (sys.argv[1] != "c" and sys.argv[1] != "d"):
            Shamir.imprimeUso("La entrada es incorrecta")

    def imprimeUso(mensaje):
        """
        Imprime cuáles son los argumentos que 
        se esperan recibir para que el programa funcione.
        
        Parametros:
        mensaje -- error de entrada capturado
        """
        print ("\n USO: " + mensaje)
        doc = "\n CIFRAR: \n\n"        
        doc += "   >>> c nombre_evaluaciones n t archivo_claro \n\n"
        doc += " Dónde 'n' es el número de evaluaciones requeridas (n > 2) \n"
        doc += " Y 't' son los puntos mínimos para descifrar (1 < t ≤ n) ​\n\n"
        doc += " DECIFRAR: \n\n   >>> d archivo_evaluaciones archivo_cifrado \n"
        sys.exit(doc)

    def verificaCifrar(arr):
        """
        Verifica que la entrada para cifrar sea correcta y 
        llama al metodo correspondiente para ello.
        
        Verifica que el archivo claro exista y que los 
        valores de n y t sean correctos,
        en caso de que no, imprime el modo de uso.
        Asume que el metodo es destructivo y no verifica 
        si el nombre de destino ya existe.
        
        Parametros:
        arr -- la entrada con los argumentos recibidos
        Excepciones:
        SystemExit -- Si la entrada recibida no es válida
        """
        n = int(arr[1])
        t = int(arr[2])
        if (n < 2):
            Shamir.imprimeUso("El número de evaluaciones requeridas es n > 2 ")        
        if (t > n or t < 2):
            Shamir.imprimeUso("El mínimo número de evaluaciones a descifrar es​ 1 < t ≤ n")                
        if not os.path.isfile(arr[3]):
            Shamir.imprimeUso("No se encontró el archivo de texto claro")            
        else:                      
            Cifrar.getCifrado(arr[0], n, t, arr[3])  
    
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
            Shamir.imprimeUso("No se encontró el archivo con las evaluaciones")        
        if not os.path.isfile(arr[1]):
            Shamir.imprimeUso("No se encontró el archivo de texto cifrado")        
        else:
            Descifrar.getDescifrado(arr[0], arr[1])

if __name__ == "__main__":
    Shamir.verifica()