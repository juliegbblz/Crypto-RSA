import random

from sympy import true

from euclide_etendu import exponentiation_modulaire


def generation_nombre_premier(nbits):
    premier=random.getrandbits(nbits)
    return premier

def temoin(a,premier):
    x[0]=exponentiation_modulaire(a,u,premier)
    for i in range(1,t):
        x[i]=(x[i-1]**2)%premier
        if x[i]==1 and x[i-1]!=1 and x[i-1]!=premier-1:
            return True
    if x[t]!=1:
        return True
    return False

def pseudo_premier(premier):
    for j in range(1,50):
        a=random.randint(1,premier-1)
        if temoin(a,premier):
            return False
        else:
            return True


