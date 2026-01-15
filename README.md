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
- Modules standard Python (random, string, os)

## Installation et utilisation

### Installation

```bash
# Cloner le projet
git clone https://github.com/votre-nom/generateur-mdp.git
cd generateur-mdp

# Aucune dépendance externe requise
```

### Lancement

```bash
python3 main.py
```

## Guide d'utilisation

1. Lancez le programme avec `python3 main.py`
2. Choisissez une option dans le menu :
   - **1. Générer** : Créer un nouveau mot de passe
   - **2. Analyser** : Vérifier la force d'un mot de passe existant
   - **3. Historique** : Afficher les derniers mots de passe générés
   - **4. Quitter** : Fermer l'application

### Exemple d'utilisation

```
=== Générateur de Mots de Passe ===
1. Générer un mot de passe
2. Analyser la force
3. Afficher l'historique
4. Quitter

Votre choix : 1
Longueur (8-50) : 16
Inclure majuscules (O/N) : O
Inclure minuscules (O/N) : O
Inclure chiffres (O/N) : O
Inclure symboles (O/N) : O

Mot de passe généré : aB7#kL2$mN9@pQ5!
Force : Très Fort
 Sauvegardé dans l'historique
```

## Structure du projet

```
generateur-mdp/
│
├── main.py              # Code principal
├── historique.txt       # Fichier de sauvegarde (généré automatiquement)
├── README.md            # Documentation
└── .gitignore           # Fichiers ignorés par Git
```

## Tests effectués

- Génération avec tous les types de caractères
- Génération avec un seul type de caractère
- Validation des longueurs (min 8, max 50)
- Gestion des erreurs de saisie
- Sauvegarde et lecture de l'historique
- Calcul correct des scores de force

## Équipe

- **Nom Prénom** - Développeur principal
- **Nom Prénom** - Développeur
- **Nom Prénom** - Développeur

### Répartition des tâches

- **Nom Prénom** : Fonctions de génération et menu
- **Nom Prénom** : Analyse de force et validation
- **Nom Prénom** : Historique et sauvegarde

## Contexte pédagogique

Projet réalisé dans le cadre du module **1PRJ1 - Projet Python Fondamental** à l'École IT (Bachelor 1, Unité 1).

**Objectifs pédagogiques :**
- Conception et développement d'un programme Python complet
- Application des bonnes pratiques de programmation (PEP 8)
- Gestion de projet avec Git
- Documentation technique

## Licence

Projet étudiant - École IT - 2025-2026

## Contact

Pour toute question : votre.email@ecole-it.com
message.txt
4 Ko
