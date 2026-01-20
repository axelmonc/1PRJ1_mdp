# 1PRJ1_mdp
# Générateur de Mots de Passe Sécurisés

##  Description

Application Python permettant de générer des mots de passe sécurisés avec analyse de force et historique. Développé dans le cadre du module 1PRJ1 - Projet Python Fondamental.

## Fonctionnalités

- Génération de mots de passe personnalisables (8-50 caractères)
- Choix des types de caractères (majuscules, minuscules, chiffres, symboles)
- Analyse de la force du mot de passe (Faible/Moyen/Fort/Très Fort)
- Historique des 10 derniers mots de passe générés
- Sauvegarde persistante dans un fichier
- Interface console intuitive avec menu

## Prérequis

- Python 3.8 ou supérieur
- Modules standard Python (random, string, datetime)


### Installation

```bash
# Cloner le projet
git clone https://github.com/axelmonc/1PRJ1_mdp.git
cd 1PRJ1_mdp

```

### Lancement

```bash
python3 main.py
```

## Guide d'utilisation

1. Lancez le programme avec `python3 main.py`
2. Choisissez une option dans le menu :
   - **1. Générer un mot de passe** : Créer un nouveau mot de passe 
   - **2. Analyser la force d'un mot de passe** : Vérifie la force du mot de passe
   - **3. ajouter un compte** : ajoute un mot de passe dans un compte du fichier json
   - **5. lister les comptes** : Afficher la liste des comptes et mots de passe présent dans le fichier json
   - **5. rechercher un compte** : recherche si un compte et son mot de passe sont présent dans le fichier json  
   - **6. Calculer les statistiques** : affiche la force et le compte du mot de passe
   - **7. sauvegarder un mot de passe** : enregistre automatiquement les comptes et leur mot de passe dans le fichier json  
   - **0. Quitter** : Ferme l'application

### Exemple d'utilisation

```
=== Générateur de Mots de Passe ===
1. Générer un mot de passe
2. Analyser la force
3. Afficher l'historique
4. Quitter

Votre choix : 1
Longueur (8-50) : 16
Inclure majuscules (Oui/Nnon) : Oui
Inclure minuscules (Oui/Non) : Oui
Inclure chiffres (Oui/Non) : Oui
Inclure symboles (Oui/Non) : Oui

Mot de passe généré : aB7#kL2mN9@pQ5!
Score : 100/100
Force : Très Fort
 Sauvegardé dans l'historique
```

## Structure du projet

```
generateur-mdp/
│
├── main.py              # Code principal
├── donnees.json       # Fichier de sauvegarde (généré automatiquement)
├── README.md            # Documentation

```

## Tests effectués

- Génération avec tous les types de caractères
- Génération avec un seul type de caractère
- Validation des longueurs (min 8, max 50)
- Gestion des erreurs de saisie
- Sauvegarde et lecture de l'historique
- Calcul correct des scores de force
- sauvegarde avec succès des copptes dans le fichier

## Équipe

- **Monchicourt Axel** - Développeur principal
- **Sidibe Aboubakr Sidick** - Développeur
- **Kouadio Oceane** - Développeur

### Répartition des tâches

- **Monchicourt Axel** : Fonctions de génération, menu et interface, ajouter les comptes et nettoyage général du code 
- **Sidibe Aboubakr Sidick** : Fonction d'analyse de force, sauvegarde des fichiers et écriture du README 
- **Kouadio Oceane** : Fonction lister, calculer les statisques, rechercher et préparation de l'oral

## Contexte pédagogique

Projet réalisé dans le cadre du module **1PRJ1 - Projet Python Fondamental** à l'École IT (Bachelor 1, Unité 1).

**Objectifs pédagogiques :**
- Conception et développement d'un programme Python complet
- Application des bonnes pratiques de programmation (PEP 8)
- Gestion de projet avec Git
- Documentation technique

##  Technologies utilisées

- Pycharm
- Modules : json, random, import, string, datetime
- Git Bash

## Licence

Projet étudiant - École IT - 2025-2026

## Contact

Pour toute question : 111916@ecole-it.com


