import unittest

from sys import path
path.append("../..")
#from src.main.myp.cifrar import Cifrar

class TestCifrar(unittest.TestCase):

    cont = 'myp3'    
    k_sha = b'\x84"\x9d\xa6\xc7\xac\x1f\x0f\x8b\xa4\x93\x006\x88\xad\xd7\xa73y\xdb\xd3\xfc\x8d\xde\xce\xca}\xbd\xdb\x0c\x14\x9f'    
    k = 59766456883749173848673077665442509862002948593001831552716989880684327474335

    @unittest.skip("Conflicto con los modulos")
    def test_sha(self):
        """
        Verifica que la función de dispersión obtiene la 
        dispersión correcta de la contraseña.

        Compara que la llave producida por sha() dados ciertos 
        valores y la llave k_sha esperada sean iguales.        
        """
        self.assertEqual(Cifrar.sha(self.cont), self.k_sha)  
        
     
if __name__ == "__main__":
    unittest.main()