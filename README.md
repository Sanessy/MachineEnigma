# Cryptographie & Blockchain - Machine Enigma

## Description

Ce projet, réalisé dans le cadre du module de M2 MIAGE de Cryptographie & Blockchain, implémente une simulation de la machine **Enigma**, utilisée principalement pendant la Seconde Guerre mondiale pour chiffrer et déchiffrer des messages. Le programme permet de simuler les étapes suivantes :

1. Initialisation de la machine Enigma, avec une première substitution de caractères pour le texte à chiffrer.
2. Configuration des rotors.
3. Chiffrement et déchiffrement des messages.

## Langage

Ce projet est développé en **Python** version 3.10.12.


### 1. Cloner le dépôt

Ouvrez une fenêtre de terminal (PowerShell) et clonez le dépôt Git en exécutant la commande suivante :

```bash
git clone https://github.com/Sanessy/MachineEnigma.git
```

Une fois le dépôt cloné, déplacez-vous dans le répertoire du projet avec la commande suivante :

```bash
cd <CHEMIN_VERS_LE_REPERTOIRE>
```

Excuter la machine enigma

```bash
python enigma.py ou .\enigma.py

```
## Prérequis

-Python 3 (version 3.10.12 recommandée).
-Aucune dépendance externe spécifique n'est requise.
  
## Exemple d'utilisation

1. Le programme vous demandera de saisir dans un premier temps de chiffrer :

    1.1 **Phrase à chiffrer** : par exemple, `cryptographie`.  
    1.2 **Configuration initiale** : une série de lettres pour une première substitution, par exemple `qsdfghjklmwxc`.  
    
    _NB : le nombre de lettres saisies pour la substitution doit concorder avec le nombre de lettres du texte que l'on souhaite chiffrer_.
    
    1.3 **Positions des rotors** : entrez les positions initiales des trois rotors, par exemple `1`, `3`, `5`.

2. Le programme retourne le message chiffré après application des étapes de chiffrement de l'algorithme
   
4. Le programme vous demandera si vous souhaitez déchiffrer le message : répondez par "oui" ou "non".
Pour tester le déchiffrement dans un contexte representatif de Enigma, vous pouvez ouvrir un deuxième terminal et exécuter le programme avec la même configuration initiale (série de lettres de substitution, positions des rotors).

6. Resultat : Le texte déchiffré correspond bien au texte initialement chiffré.
   

## Terminal 1 
<img width="626" alt="enigmaterminalvscode" src="https://github.com/user-attachments/assets/25f741cb-c738-4a08-aaaa-5e83c80b380c">

## Terminal 2
<img width="555" alt="enigmaterminal" src="https://github.com/user-attachments/assets/e15cfc26-5aa4-4d59-9f5a-63bf8077e1d3">




