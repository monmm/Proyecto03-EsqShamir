import random
from decimal import *

class Evalua:

    global campo 
    campo = 10**5 

    def getEvaluaciones(n, t, k):               
        t_ind = Evalua.getCoeficiente(t, k) 
        evaluaciones = [] 
      
        for i in range(1, n+1): 
            rango = random.randrange(1, campo) 
            evaluaciones.append((rango, Evalua.getPolinomio(rango,t_ind))) 
      
        return evaluaciones    

    def getCoeficiente(t, k):               
    
        coef = [random.randrange(0, campo) for _ in range(t-1)] 
        coef.append(k) 
      
        return coef

    def getPolinomio(x, coef):               
        return sum([x**(len(coef)-i-1) * coef[i] for i in range(len(coef))])                

    def toString(shares):
        s = ""     
        c = 0
        for i in shares:
            if c < len(shares)-1:
                s += str(i) + "\n"
                c += 1
            else:
                s += str(i)
        return s