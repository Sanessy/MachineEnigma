# Cryptographie & Blockchain - Machine Enigma

## Description

Ce projet dans le cadre du module de M2 MIAGE de Cryptographie & Blockchain implémente une simulation de la machine **Enigma**, utilisée principalement pendant la Seconde Guerre mondiale pour chiffrer et déchiffrer des messages. Le programme permet dans un premier temps d'initialiser la machine Enigma en réalisant une substitution initiale de caractères avec le texte que l'on souhaite chiffrer. Le programme permet par la suite de configurer les rotors puis de chiffrer et déchiffrer des messages.

## Langage

Ce projet est écrit en **Python** 3.10.12 dans Google Colab

## Cloner le projet

Pour cloner ce projet sur votre machine, exécutez la commande suivante : git clone https://github.com/

## Prérequis

- Python 3
- Aucune dépendance externe spécifique n'est requise.
- 
## Exemple d'utilisation

1. Le programme vous demandera de saisir dans un premier temps :

    1.1 **Phrase à chiffrer** : par exemple, `cryptographie`.  
    1.2 **Configuration initiale** : une série de lettres pour une première substitution, par exemple `qsdfghjklmwxc`.  
    
    _NB : le nombre de lettres saisies pour la substitution doit concorder avec le nombre de lettres du texte que l'on souhaite chiffrer_.
    
    1.3 **Positions des rotors** : entrez les positions initiales des trois rotors, par exemple `1`, `3`, `5`.

2. Le programme retourne le message chiffré après application des étapes
3. Le programme vous demande si vous souhaitez déchiffrer le message : "oui" ou "non"


