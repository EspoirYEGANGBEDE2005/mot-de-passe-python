import random
import string

def generer_mot_de_passe(longueur, inclure_majuscules, inclure_chiffres, inclure_speciaux):
    caracteres = string.ascii_lowercase
    if inclure_majuscules:
        caracteres += string.ascii_uppercase
    if inclure_chiffres:
        caracteres += string.digits
    if inclure_speciaux:
        caracteres += string.punctuation

    if longueur < 1:
        print("La longueur du mot de passe doit être au moins 1.")
        return None

    mot_de_passe = ''.join(random.choice(caracteres) for _ in range(longueur))
    return mot_de_passe

def main():
    print("Générateur de mot de passe sécurisé")

    longueur = int(input("Entrez la longueur du mot de passe : "))
    inclure_majuscules = input("Inclure des majuscules ? (oui/non) : ").strip().lower() == 'oui'
    inclure_chiffres = input("Inclure des chiffres ? (oui/non) : ").strip().lower() == 'oui'
    inclure_speciaux = input("Inclure des caractères spéciaux ? (oui/non) : ").strip().lower() == 'oui'

    mot_de_passe = generer_mot_de_passe(longueur, inclure_majuscules, inclure_chiffres, inclure_speciaux)

    if mot_de_passe:
        print(f"Votre mot de passe généré est : {mot_de_passe}")
    else:
        print("Impossible de générer le mot de passe avec les paramètres fournis.")

if __name__ == "__main__":
    main()
