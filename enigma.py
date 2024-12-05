import string

alphabet_initial = list(string.ascii_lowercase)  # Liste des lettres de l'alphabet en minuscules
alphabet_initial_inverse = alphabet_initial[::-1]  # Liste des lettres de l'alphabet en ordre inverse
caracteres_speciaux = string.punctuation + string.whitespace  # Liste des caractères spéciaux, incluant la ponctuation et les espaces

# CLASS ROTOR
class Rotor:
    def __init__(self, position_depart, alphabet):
        # Initialisation d'un rotor avec sa position de départ et l'alphabet associé
        # position_depart : Position initiale du rotor dans l'alphabet
        # alphabet : Alphabet utilisé par le rotor, qui sera modifié lors de chaque rotation
        self.position_depart = position_depart
        self.alphabet = alphabet
        self.position_actuelle = position_depart  # La position actuelle du rotor est initialisée à la position de départ

    def tourne(self):
        # Faire tourner le rotor d'une position, effectuant un déplacement circulaire de l'alphabet
        # Cela modifie la position actuelle du rotor, de manière à ce qu'il se déplace d'une lettre à la fois
        self.alphabet = self.alphabet[1:] + [self.alphabet[0]]
        self.position_actuelle = (self.position_actuelle % 26) + 1  # Mise à jour de la position actuelle du rotor (toujours entre 1 et 26)

    def transforme(self, caractere, inverse=False):
        # Transforme un caractère selon l'alphabet du rotor, en fonction de la direction (inverse ou non)
        # Si 'inverse' est True, on effectue l'opération dans l'ordre inverse, sinon dans l'ordre normal
        if caractere in alphabet_initial:
            if inverse:
                # Si inverse est True, on trouve la position du caractère dans l'alphabet du rotor et on le mappe à l'alphabet initial
                index_rotor = self.alphabet.index(caractere)
                return alphabet_initial[index_rotor]
            else:
                # Si inverse est False, on mappe directement le caractère de l'alphabet initial vers l'alphabet du rotor
                index_alphabet = alphabet_initial.index(caractere)
                return self.alphabet[index_alphabet]
        else:
            # Si le caractère n'est pas une lettre (par exemple, un caractère spécial), on le retourne tel quel sans transformation
            return caractere

# FONCTION DE CRÉATION DES ROTORS
def creation_rotor(position_depart):
    # Crée un rotor avec une position de départ donnée
    # L'alphabet du rotor est généré en décalant l'alphabet initial à partir de la position de départ
    rotor_alphabet = alphabet_initial[position_depart - 1:] + alphabet_initial[:position_depart - 1]
    return Rotor(position_depart, rotor_alphabet)

# SUBSTITUTION (PLUGBOARD)
def applique_substitution(caractere, substitution_initiale, substitution_inverse):
    # Applique une substitution à un caractère selon les mappings définis par le plugboard
    # Le plugboard est un système de câblage qui échange les lettres selon une configuration donnée
    if caractere in substitution_initiale:
        index = substitution_initiale.index(caractere)
        return substitution_inverse[index]
    return caractere

# CLASS ENIGMA MACHINE
class EnigmaMachine:
    def __init__(self, rotors, plugboard_substitutions):
        # Initialisation de la machine Enigma avec la configuration des rotors et les substitutions du plugboard
        # rotors : Liste des rotors configurés pour la machine
        # plugboard_substitutions : Le couple de listes de substitutions initiale et inverse pour le plugboard
        self.rotors = rotors
        self.plugboard_substitutions = plugboard_substitutions

    def chiffre_dechiffre_texte(self, phrase):
        # Fonction principale pour chiffrer ou déchiffrer un texte en fonction de la configuration de la machine Enigma
        # Cette fonction applique successivement les transformations via les rotors, la réflexion et le plugboard
        phrase_finale = []  # Liste pour stocker les caractères chiffrés ou déchiffrés
        substitution_initiale, substitution_inverse = self.plugboard_substitutions  # Obtenons les substitutions du plugboard

        for caractere in phrase:
            if caractere in caracteres_speciaux:
                # Si le caractère est un caractère spécial (ponctuation, espace), on l'ajoute sans transformation
                phrase_finale.append(caractere)
            else:
                # Applique la substitution initiale via le plugboard (première transformation)
                caractere = applique_substitution(caractere, substitution_initiale, substitution_inverse)

                # Transformation à travers les rotors dans l'ordre normal
                for rotor in self.rotors:
                    caractere = rotor.transforme(caractere)

                # Réflexion dans le miroir de la machine Enigma : on effectue un renversement de l'alphabet
                if caractere in alphabet_initial:
                    index = alphabet_initial.index(caractere)
                    caractere = alphabet_initial_inverse[index]

                # Re-transformation à travers les rotors dans l'ordre inverse
                for rotor in reversed(self.rotors):
                    caractere = rotor.transforme(caractere, inverse=True)

                # Applique la substitution inverse via le plugboard (deuxième transformation)
                caractere = applique_substitution(caractere, substitution_initiale, substitution_inverse)

                phrase_finale.append(caractere)  # Ajoute le caractère transformé à la phrase finale

                # Faire tourner le rotor le plus à gauche après chaque transformation de caractère
                self.rotors[0].tourne()

                # En fonction de la position des rotors, certains peuvent tourner automatiquement après chaque rotation
                for i in range(len(self.rotors) - 1):
                    if self.rotors[i].position_actuelle == 1:
                        self.rotors[i + 1].tourne()
                    else:
                        break

        return ''.join(phrase_finale)  # Retourne le texte final sous forme de chaîne de caractères

# CONFIGURATION INITIALE
# Demander à l'utilisateur la phrase à chiffrer et la configuration du plugboard
phrase_a_chiffrer = input("Entrez la phrase à chiffrer : ").lower().replace(" ", "")  # Suppression des espaces et mise en minuscule

# Demander la configuration initiale pour le plugboard (substitution)
caracteres_substitution = input(f"Entrez les {len(phrase_a_chiffrer)} lettres permettant la configuration initiale par substitution : ").lower()
while len(caracteres_substitution) != len(phrase_a_chiffrer) or any(c in caracteres_speciaux for c in caracteres_substitution):
    caracteres_substitution = input(f"Entrée invalide. Veuillez entrer exactement {len(phrase_a_chiffrer)} caractères sans espaces ni ponctuation : ").lower()

# Création du dictionnaire de substitution du plugboard (lettres échangées)
plugboard_dict = {}
for lettre1, lettre2 in zip(phrase_a_chiffrer, caracteres_substitution):
    if lettre1 not in plugboard_dict and lettre2 not in plugboard_dict and lettre1 != lettre2:
        plugboard_dict[lettre1] = lettre2
        plugboard_dict[lettre2] = lettre1

# Préparation des listes de substitution initiale et inverse
substitution_initiale = list(plugboard_dict.keys())
substitution_inverse = [plugboard_dict[lettre] for lettre in substitution_initiale]
plugboard_substitutions = (substitution_initiale, substitution_inverse)

# Demander à l'utilisateur la position des rotors
rotors = [creation_rotor(int(input(f"Entrez la position initiale du rotor {i+1} (entre 1 et 26) : "))) for i in range(3)]

# Créer la machine Enigma avec les rotors et la substitution du plugboard
machine = EnigmaMachine(rotors, plugboard_substitutions)

# Chiffrer le message
phrase_chiffree = machine.chiffre_dechiffre_texte(phrase_a_chiffrer)
print("Phrase chiffrée :", phrase_chiffree)

# Demander si l'utilisateur souhaite déchiffrer le message
dechiffrer = input("Souhaitez-vous déchiffrer le message ? (oui/non) : ").strip().lower()
if dechiffrer == "oui":
    # Recréer la machine Enigma avec les mêmes paramètres pour déchiffrer
    rotors = [creation_rotor(rotor.position_depart) for rotor in machine.rotors]
    machine = EnigmaMachine(rotors, plugboard_substitutions)
    phrase_dechiffree = machine.chiffre_dechiffre_texte(phrase_chiffree)
    print("Phrase déchiffrée :", phrase_dechiffree)
else:
    print("Fin du processus. Vous pouvez maintenant utiliser la phrase chiffrée comme bon vous semble.")
