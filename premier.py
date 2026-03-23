import random

from euclide_etendu import exponentiation_modulaire


def generation_nombre(nbits):
    premier=random.getrandbits(nbits)
    return premier

def temoin(a,premier):
    if premier < 4:
        return False

    u = premier - 1
    t = 0
    while u % 2 == 0:
        u //= 2
        t += 1

    x = [0] * (t + 1)
    x[0] = exponentiation_modulaire(a, u, premier)
    if x[0] == 1 or x[0] == premier - 1:
        return False

    for i in range(1, t + 1):
        x[i] = (x[i - 1] ** 2) % premier
        if x[i] == premier - 1:
            return False
        if x[i] == 1 and x[i - 1] != 1 and x[i - 1] != premier - 1:
            return True

    return True

def Miller_Rabin(premier):
    if premier in (2, 3):
        return True
    if premier <= 1 or premier % 2 == 0:
        return False

    for j in range(1,50):
        a=random.randint(2,premier-2)
        if temoin(a,premier):
            return False
    return True

def generateur_premier(nbits):
    flag = True
    nb = 0
    while flag:
        nb = generation_nombre(nbits)
        if Miller_Rabin(nb):
            flag = False
    return (nb)
