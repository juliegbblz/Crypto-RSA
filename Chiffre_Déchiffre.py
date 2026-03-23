from choix_cles import test_chiffre
from premier import generateur_premier

p=generateur_premier(512)
q=generateur_premier(512)

def recuperation_texte(nom_fichier):
    try:
        with open(nom_fichier, 'r', encoding='utf-8') as fichier:
            contenu = fichier.read()
            entier = int(contenu)
            return entier
    except FileNotFoundError:
        print(f"Le fichier {nom_fichier} n'a pas été trouvé.")
        return None

def depot_texte(entier, nom_fichier):
    texte = str(entier)
    with open(nom_fichier, 'w', encoding='utf-8') as fichier:
        fichier.write(texte)

def chiffrer_texte(nom_fichier):
    entier = recuperation_texte(nom_fichier)
    return test_chiffre(entier,p,q)

def dechiffre_texte(enier, nom_fichier):
    depot_texte(enier, nom_fichier)
