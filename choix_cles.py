from premier import generateur_premier
from euclide_etendu import generer_cles_RSA, chiffrer, dechiffrer


p=generateur_premier(512)
q=generateur_premier(512)

def test_chiffre(message, p, q, e):
    cles_publiques, cles_privees = generer_cles_RSA(p, q, e)
    m = chiffrer(message, cles_publiques)
    return m, cles_privees
    
def test_dechiffre(message, cles_privees):
    message_dechiffre = dechiffrer(message, cles_privees)
    return message_dechiffre

message_chiffre, cles_privees = test_chiffre(500, p, q, 9)
print("Message chiffré:", message_chiffre)
print("Message déchiffré:", test_dechiffre(message_chiffre, cles_privees))