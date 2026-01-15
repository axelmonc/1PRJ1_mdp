- [X] test generer_mdp() : WAKY!muga!fUji@SuwAbi4
- [ ] test analyser_force() :
     Erreur :
     File "c:\Users\sidib\Downloads\PRJ1.ipynb", line 5, in <module>
    "execution_count": null,
                       ^^^^
      
    def analyser_force(mot_de_passe):
      #fonction qui calcule l'entropie et verifie les critères
     #Validation de la longueur obligatoire (8-64)
    longueur = len(mot_de_passe)
    if longueur < 8 or longueur > 64:
        return 0, "Invalide (Doit faire entre 8 et 64 caractères.)"
    score = 0

     #Bonus de longueur (20 points max)
     #On donne 2 points par caractère au-dessus de 7.
    points_longueur = (longueur - 7) * 2
    if points_longueur > 20:
        points_longueur = 20
    #On ajoute les points au score global ici:
    score += points_longueur

     #Etat de détection
    a_voyelle = False
    a_consonne = False
    a_majuscule = False
    a_chiffre = False
    a_symbole = False

     #Listes de référence (Variables demandées)
    voyelles = "aeiouyAEIOUY"
    consonnes = "bcdfghjkmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
    chiffres = "23456789"  # Exclusion du 0 et 1 selon tes critères
    symboles = "@_-"

     #Analyse par boucle 
    for char in mot_de_passe:
        if 'A' <= char <= 'Z':
            a_majuscule = True
        if char in voyelles:
            a_voyelle = True
        elif char in consonnes:
            a_consonne = True
        if char in chiffres:
            a_chiffre = True
        if char in symboles:
            a_symbole = True
      
     #Attribution des points (16 points par critère rempli)
    if a_voyelle:   score += 16
    if a_consonne:  score += 16
    if a_majuscule: score += 16
    if a_chiffre:   score += 16
    if a_symbole:   score += 16
     #Détermination du niveau final
    if score < 50:
        niveau = "Faible"
    elif score < 80:
        niveau = "Moyen"
    else:
        niveau = "Très Fort"
     #On retourne les valeurs pour pouvoir les réutiliser
    return int(score), niveau

     #Exemples de tests et affichage 
     #On utilise une petite fonction d'affichage pour présenter les résultats proprement
def tester_mdp(mdp):
    res_score, res_niveau = analyser_force(mdp)
    if res_score == 0:
        print(f"MOT DE PASSE: {mdp} -> {res_niveau}")
    else:
        print(f"Le score du mot de passe '{mdp}' est {res_score}/100 et son niveau est : {res_niveau}")

tester_mdp("WAKY!muga!fUji@SuwAbi4")

NameError: name 'null' is not defined
- [ ] test ajouter_compte() : 
- [ ] test lister_comptes() :
- [ ] test rechercher() :
- [ ] test calculer_stats() :
- [X] test sauvegarder() : C:/Users/sidib/.spyder-py3/sanstitre1.py --wdir
Fichier sauvegardé avec succès 
