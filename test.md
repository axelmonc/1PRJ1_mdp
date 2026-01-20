- [X] test generer_mdp() :

```
generer_mdp()
>>>Combien de caractères pour le mot de passe (8-64) : 22
>>>WAKY!muga!fUji@SuwAbi4
 ```
 
- [X] test analyser_force() :

```
mdp = WAKY!muga!fUji@SuwAbi4
analyser_force(mdp)
>>> (100, 'Très Fort')
 ```

- [X] test ajouter_compte() :

```
ajouter_compte()
>>>CHOISIR :
1. generer un mot de passe
2. entrer un mot de passe
Entrer votre choix : 1
Combien de caractères pour le mot de passe (8-64) : 22
Le mot de passe est : FuVa8mE7bo7bYSEjE8DapU
*VEUILLEZ SELECTIONNER UNE CATEGORIE*
1. Reseaux sociaux
2. Banque
3. Email
4. Travail
5. Autre

Entrer votre choix : 1
Entrer le nom du compte : test
Entrer le nom du site : testbq.com
________votre compte a bien été ajouté_______
 ```

- [X] test lister_comptes() :
```
lister_comptes()
>>>*********LISTE DES COMPTES*********

Compte :  1

Categorie : Banque
Compte : test
Site : testbq.com
Mot de passe : dU@fAMAsU5BA
Date : 2026-01-20 09:48:09.852532
Score : 90
```

- [X] test_rechercher() :

```
test_rechercher()
>>>******* QUE VOULEZ-VOUS RECHERCHER ? *******
1. Rechercher par catégorie
2. Rechercher par nom de site
Votre choix : 1
Entrer votre recherche : Banque

___________ Résultat de la Recherche _________
Categorie : Banque
Compte : test
Site : testbq.com
Mot de passe : dU@fAMAsU5BA
Date : 2026-01-20 09:48:09.852532
Score : 90
--------------------
```

- [X] test calculer_stats() :

```
calculer_stats()
>>> ==================================================
              STATISTIQUES GLOBALES               
==================================================
Nombre total de comptes : 1
Score de sécurité moyen : 90.0/100

--- Répartition par catégorie ---
Banque          : 1 (100.0%)

--- ALERTES SÉCURITÉ ---
Faibles (<50)  : 0
Anciens (>90j) : 0
En double      : 0 mot(s) de passe utilisé(s) plusieurs fois
```

- [X] test sauvegarder() :
```
test_sauvegarder()
>>>C:/Users/sidib/.spyder-py3/sanstitre1.py --wdir Fichier sauvegardé avec succès
```
