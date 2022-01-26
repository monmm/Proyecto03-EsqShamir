import unittest

from sys import path
path.append("../..")
from src.main.myp.evalua import Evalua

class TestEvalua(unittest.TestCase):
    
    evaluaciones = [(22788, 59766456883749173848673077665442509862002948593001831552716989905587189508511), 
                    (97563, 59766456883749173848673077665442509862002948593001831552716990337117405776386), 
                    (58900, 59766456883749173848673077665442509862002948593001831552716990047042221603935), 
                    (88792, 59766456883749173848673077665442509862002948593001831552716990258739686897087), 
                    (15485, 59766456883749173848673077665442509862002948593001831552716989892183795061850)]
    rep_cadena =  '(22788, 59766456883749173848673077665442509862002948593001831552716989905587189508511)\n' 
    rep_cadena += '(97563, 59766456883749173848673077665442509862002948593001831552716990337117405776386)\n' 
    rep_cadena += '(58900, 59766456883749173848673077665442509862002948593001831552716990047042221603935)\n'
    rep_cadena += '(88792, 59766456883749173848673077665442509862002948593001831552716990258739686897087)\n'
    rep_cadena += '(15485, 59766456883749173848673077665442509862002948593001831552716989892183795061850)'
    
    def test_toString(self):
        """
        Verifica que la representación en cadena de una lista de 
        evaluaciones se obtiene correctamente.

        Compara que la cadena producida por toString() dados ciertos 
        valores y la representacion en cadena esperada sean iguales.        
        """
        self.assertEqual(Evalua.toString(self.evaluaciones), self.rep_cadena)  
        
     
if __name__ == "__main__":
    unittest.main()