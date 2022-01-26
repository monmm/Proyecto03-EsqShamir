# Utilizamos random para la lista aleatoria de coeficientes.
import random

class Evalua:

    global campo 
    campo = 10**5 

    def getEvaluaciones(n, t, k):
        """
        Divide la clave 'k' dada en 'n' fragmentos 
        con un umbral mínimo de 't' para recuperarlo, 
        utilizando el algoritmo de SSS.

        Parametros:
        n -- el número de evaluaciones del polinomio.
        t -- el número de fragmentos del polinomio.
        k -- la clave, constante del polinomio.
        """               
        t_ind = Evalua.getCoeficiente(t, k)        
        evaluaciones = [] 
      
        for i in range(1, n+1): 
            val = random.randrange(1, campo) 
            evaluaciones.append((val, Evalua.getPolinomio(val, t_ind))) 
      
        return evaluaciones    

    def getCoeficiente(t, k):               
        """
        Genera una lista aleatoria de coeficientes para 
        un polinomio con grado 't-1', cuya constante es 'k'.

        Parametros:
        t -- los fragmentos del polinomio.
        k -- la clave a ocultar en el polinomio.
        """
        coef = [random.randrange(0, campo) for _ in range(t-1)] 
        coef.append(k) 
      
        return coef

    def getPolinomio(x, coef):
        """
        Genera un punto en el gráfico del polinomio dado 
        por la lista de coeficientes.

        Parametros:
        x -- el punto del polinomio.
        coef -- la lista de coeficientes.
        """             
        punto = 0    
        for indice, evaluacion in enumerate(coef[::-1]):
            punto += x ** indice * evaluacion
        return punto              

    def toString(eval):
        """
        Regresa la representación en cadena de las 
        evaluaciones del polinomio.

        Parametros:
        eval -- las evaluaciones del polinomio.
        """
        s = ""     
        c = 0
        for i in eval:
            if c < len(eval)-1:
                s += str(i) + "\n"
                c += 1
            else:
                s += str(i)
        return s