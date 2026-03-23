def euclide_etendu(a,b):
    if b == 0:
        return a, 1, 0
    else:
        d, x1, y1 = euclide_etendu(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return d, x, y
    
    

 
    
def exponentiation_modulaire(a,b,n):
    resultat = 1
    a = a % n
    while b > 0:
        if b % 2 == 1:
            resultat = (resultat * a) % n
        a = (a * a) % n
        b //= 2
    return resultat


def pgcd(a, b):
    return euclide_etendu(a, b)[0]

    
def generer_cles_RSA(p, q, e):
    n = p * q
    phi_n = (p - 1) * (q - 1)

    if e <= 1 or e >= phi_n or pgcd(e, phi_n) != 1:
        e = 65537
        if e >= phi_n or pgcd(e, phi_n) != 1:
            e = 3
            while e < phi_n and pgcd(e, phi_n) != 1:
                e += 2
            if e >= phi_n:
                raise ValueError("Aucun exposant e inversible modulo phi(n)")

    d = pow(e, -1, phi_n)
    cle_publique = (e, n)
    cle_privee = (d, n)
    return cle_publique, cle_privee



def chiffrer(message, cle_publique):
    e, n = cle_publique
    message_chiffre = [exponentiation_modulaire(message, e, n)]
    return message_chiffre



def dechiffrer(message_chiffre, cle_privee):
    d, n = cle_privee
    message_dechiffre = [exponentiation_modulaire(m, d, n) for m in message_chiffre]
    return message_dechiffre
