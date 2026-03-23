from premier import generateur_premier
from euclide_etendu import generer_cles_RSA, chiffrer, dechiffrer


p=generateur_premier(512)
q=generateur_premier(512)

def test_chiffre (message,p,q) :
    cles_publiques, cles_privees = generer_cles_RSA(p, q)
    m = chiffrer(message, cles_publiques)
    print("Message chiffré:", m)
    return m
    
def test_dechiffre (message,p,q) :
    cles_publiques, cles_privees = generer_cles_RSA(p, q)
    message_dechiffre = dechiffrer(message, cles_privees)
    print("Message dechiffré:", message_dechiffre)
    return message_dechiffre

message_chiffre = test_chiffre(75,p,q)
test_dechiffre(message_chiffre,p,q) 