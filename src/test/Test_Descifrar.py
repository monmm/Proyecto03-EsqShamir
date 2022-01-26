import unittest
from sys import path
path.append("../..")
from src.main.myp.descifrar import Descifrar

import warnings

warnings.simplefilter("ignore", ResourceWarning)

class TestCifrar(unittest.TestCase):

    evaluaciones = "src/test/data/ev.frg"
    cifrado = "src/test/data/msj.txt.aes"
    des = b'\xc2\xa1Este es el \xc3\xbaltimo proyecto!'
    datos = b'\xfea\x00\xa9\xde`\x999\xb0\xae\x85[?x\x0c\xaaUa\xee\xb6\xbb\xce\xeaJ%\x84\xa6\xee\xbf\xd4\x1b\x89\xa7\xfc8\xc2\xb4e\x91{\xc2\xd5\x97y8\xd4\xd4\xb2\x80\xd62L\xbf_\xe6V-\xb1\xa1\xefj\xe4'   
    k_byte = b'\x84"\x9d\xa6\xc7\xac\x1f\x0f\x8b\xa4\x93\x006\x88\xad\xd7\xa73y\xdb\xd3\xfc\x8d\xde\xce\xca}\xbd\xdb\x0c\x14\x9f'
    llave = 59766456883749173848673077665442509862002948593001831552716989880684327474335
    parejas = [(49396, 59766456883749173848673077665442509862002948593001831552716990010301695935163), 
         (21561, 59766456883749173848673077665442509862002948593001831552716989905380188487188), 
         (9232, 59766456883749173848673077665442509862002948593001831552716989885212197279055), 
         (45233, 59766456883749173848673077665442509862002948593001831552716989989374655996316), 
         (49999, 59766456883749173848673077665442509862002948593001831552716990013485591845926)]


    def test_getPares(self):
        """
        Verifica que las evaluaciones del archivo se obtengan correctamente.

        Compara que la lista producida por getPares() dados ciertos 
        valores y la lista de evaluaciones esperada sean iguales.        
        """
        warnings.simplefilter("ignore", ResourceWarning)
        self.assertEqual(Descifrar.getPares(self.evaluaciones), self.parejas)
    
    def test_getLlave(self):        
        """
        Verifica que podamos obtener la llave para descifrar correctamente.

        Compara que la llave producida por getLlave() dados ciertos 
        valores y la llave esperada sean iguales.        
        """
        self.assertEqual(Descifrar.getLlave(self.parejas), self.llave)

    def test_getDesencriptado(self):
        """
        Verifica que el desencriptado se obtiene correctamente.

        Compara que el mensaje en bytes producido por getDesencriptado() 
        dados ciertos valores y la el mensaje esperado sean iguales.        
        """
        self.assertEqual(Descifrar.getDesencriptado(self.k_byte, self.datos), self.des)

if __name__ == "__main__":
    unittest.main()