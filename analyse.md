Analyse détaillée des exigences et Identification des cas d'utilisation et scénarios

1. Analyse des Exigences 

A. Exigences Fonctionnelles (Ce que le système fait)
Génération : Doit supporter l'entropie personnalisée (longueur, symboles) et l'ergonomie humaine (prononçable, sans caractères ambigus).
Sécurité : L'analyseur doit décomposer le score (ex: +20 pts pour les majuscules, -10 pts si présent dans un dictionnaire).
Persistance : Lecture/Écriture en format JSON. Le système ne doit pas perdre de données si l'utilisateur ferme mal l'application.
Alertes : Le système doit comparer les dates de création avec la date actuelle 
B. Exigences Non-Fonctionnelles (Qualité du système)
Fiabilité : Gestion des exceptions (fichiers JSON vides ou corrompus).
Utilisabilité : Interface console claire avec des tableaux alignés.
Performance : La recherche et le calcul des statistiques doivent être instantanés (complexité O(n)).



2. Identification des Cas d'Utilisation 

Un cas d'utilisation décrit comment un utilisateur interagit avec le système pour atteindre un objectif.
Cas d'Utilisation

Description

Générer et Enregistrer : 

L'utilisateur demande un MDP de 16 caractères, l'examine, et décide de l'affecter à un nouveau compte "Banque".

Sécurité :

L'utilisateur consulte les statistiques pour voir quels MDP sont obsolètes ou faibles.

Maintenance des Comptes:

L'utilisateur recherche un site spécifique pour mettre à jour ou consulter le mot de passe oublié.

3. Scénarios d'Utilisation

Voici deux scénarios types pour tester la logique de ton futur algorithme :

Scénario A : Ajout d'un compte avec génération sécurisée

Utilisateur : Sélectionne l'option "Ajouter compte".
Système : Demande le nom du site (ex: GitHub) et la catégorie (ex: Travail).
Utilisateur : Demande à générer un mot de passe.
Système : Demande la longueur (ex: 20) et les options (ex: Majuscules + Chiffres + symboles).
Système : Génère, calcule un score et enregistre le tout avec la date du jour.
Résultat : Le fichier JSON est mis à jour et un message de succès s'affiche.

Scénario B : Analyse et détection de vulnérabilité

Utilisateur : Sélectionne l'option "Statistiques".
Système : Parcourt la liste des dictionnaires.
Logique interne : - Trouve deux comptes avec le même mot de passe (Alerte Doublon).
                  -Calcule qu'un compte "Email" a été créé il y a 100 jours (Alerte Ancienneté).
Système : Affiche un tableau récapitulatif : 
"Attention : 3 alertes de sécurité détectées !"

5. Erreurs probables


- Fichier absent : le programme ne trouve pas le mot de passe au démarrage.

Solution : Créer automatiquement une liste vide au lieu de planter.

- Fichier corrompu : le fichier JSON contient du texte qui n'est pas du JSON valide (ex: modification manuelle).

Solution : alerter l'utilisateur et proposer de sauvegarder le fichier corrompu sous un autre nom avant d'en créer un neuf.

- Erreur de permission : le programme n'a pas les droits d'écriture dans le dossier.
 
- Type de données incorrect : Saisir "douze" au lieu de 12 pour la longueur du mot de passe.

- Valeurs hors limites : Demander une longueur entre 8 et 64

- Champs vides : Tenter d'enregistrer un compte sans nom de site ou sans catégorie.

- Doublon de site : Essayer d'ajouter un compte "Gmail" alors qu'il existe déjà.

Solution : Demander à l'utilisateur s'il veut mettre à jour le compte existant ou annuler.

- Catégorie inexistante : Saisir une catégorie qui n'est pas dans la liste prédéfinie (Banque, Email, etc.).

- Recherche infructueuse : Rechercher un site qui n'existe pas dans la base de données.

Solution : Afficher un message clair "Aucun résultat trouvé" plutôt qu'un tableau vide.

- Erreurs de Sécurité (Logique d'analyse) : Entropie nulle, tenter d'analyser un mot de passe vide.

- Format de date invalide : Si la date dans le JSON a été modifiée manuellement et ne peut plus être lue par le module de statistiques.









