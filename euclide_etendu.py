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


pgcd =  euclide_etendu(7, 60)
print("pgcd(7, 60) =", pgcd) #bon dapres lexo 1 RSA

d= exponentiation_modulaire(7, 3, 60)
print("7^3 mod 60 =", d)

""" def generer_cle_rsa(e, phi):
    d, x, y = euclide_etendu(e, phi)
    if d != 1:
        print("e et phi ne sont pas premiers entre eux")
    else:
        return x % phi
     """
    
def generer_cles_RSA(p, q):
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = 7
    d = pow(e, -1, phi_n)
    cle_publique = (e, n)
    print(cle_publique)
    cle_privee = (d, n)
    return cle_publique, cle_privee

cles_publiques, cles_privees = generer_cles_RSA(7, 11)

print("Clés publiques (e, n):", cles_publiques)
print("Clés privées (d, n):", cles_privees)

def chiffrer(message, cle_publique):
    e, n = cle_publique
    message_chiffre = [exponentiation_modulaire(message, e, n)]
    return message_chiffre

m=chiffrer(75,cles_publiques)
print("Message chiffré:", m)

def dechiffrer(message_chiffre, cle_privee):
    d, n = cle_privee
    message_dechiffre = [exponentiation_modulaire(m, d, n) for m in message_chiffre]
    return message_dechiffre

print("Message déchiffré:", dechiffrer(m, cles_privees))