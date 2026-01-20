import random
from datetime import datetime
import json

mot_de_passes = {}
categories = ["Reseaux sociaux", "Banque", "Email", "Travail", "Autre"]
base_donnees = []


def generer_mdp():
    """
    fonction qui genere un mot de passe aleatoire selon des criteres
    :return: None
    """
    nb_cara = 0
    # va demander le nombre de caracteres a l utilisateur tant qu il n est pas compris entre 8 et 64
    while not 8 <= nb_cara <= 64:
        try:
            nb_cara = int(input("Combien de caractères pour le mot de passe (8-64) : "))
            if not 8 <= nb_cara <= 64:
                print("Erreur : La longueur doit être comprise entre 8 et 64.")
        except ValueError:
            print("Erreur : Veuillez entrer un nombre entier.")
    voyelles = ["a", "e", "i", "o", "u", "y", "A", "E", "U", "Y"]
    consonnes = ["b", "c", "d", "f", "g", "h", "j", "k", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z",
                 "B", "C", "D", "F", "G", "H", "J", "K", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Z"]
    caracteres_speciaux = ["!", "#", "@", "2", "3", "4", "5", "6", "7", "8", "9"]
    mdp = ""
    dernier_etait_special = False  # fait en sorte qu il n y ai pas 2 caracteres speciaux a la suite
    while nb_cara > 0:
        if len(mdp) == 0 or dernier_etait_special:
            mdp += random.choice(consonnes)
            mdp += random.choice(voyelles)
            nb_cara -= 2
            dernier_etait_special = False
        else:
            type = random.randint(1, 2)
            if type == 1 and nb_cara >= 2:
                mdp += random.choice(consonnes)
                mdp += random.choice(voyelles)
                nb_cara -= 2
                dernier_etait_special = False
            else:
                mdp += random.choice(caracteres_speciaux)
                nb_cara -= 1
                dernier_etait_special = True
    print("Le mot de passe est : " + mdp)
    return mdp


def analyser_force(mot_de_passe):
    """
    fonction qui calcule l'entropie et verifie les critères
    :return: int, le score (compris entre 0 et 100)
    """
    # Validation de la longueur obligatoire (Spécification : 8-64)
    longueur = len(mot_de_passe)
    if longueur < 8 or longueur > 64:
        return 0, "Invalide (Doit faire entre 8 et 64 caractères.)"
    score = 0
    # Bonus de longueur (20 points max)
    # On donne 2 points par caractère au-dessus de 7.
    points_longueur = (longueur - 7) * 2
    if points_longueur > 20:
        points_longueur = 20
    score += points_longueur
    a_voyelle = False
    a_consonne = False
    a_majuscule = False
    a_chiffre = False
    a_symbole = False
    # Listes de référence (Variables demandées)
    voyelles = "aeiouyAEIOUY"
    consonnes = "bcdfghjkmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
    chiffres = "23456789"
    symboles = "@_-"
    # Analyse par boucle simple
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
    # Attribution des points (16 points par critère rempli)
    if a_voyelle:   score += 16
    if a_consonne:  score += 16
    if a_majuscule: score += 16
    if a_chiffre:   score += 16
    if a_symbole:   score += 16
    # Détermination du niveau final
    if score < 50:
        niveau = "Faible"
    elif score < 80:
        niveau = "Moyen"
    else:
        niveau = "Très Fort"
    return int(score), niveau


def tester_mdp(mdp):
    """
    fonction qui teste un mdp
    :param mdp: str, le mot de passe
    :return: None
    """
    res_score, res_niveau = analyser_force(mdp)
    if res_score == 0:
        print(f"MOT DE PASSE: {mdp} -> {res_niveau}")
    else:
        print(f"Le score du mot de passe '{mdp}' est {res_score}/100 et son niveau est : {res_niveau}")


def ajouter_compte():
    """
    fonction qui ajoute un compte
    :return: None
    """
    print("CHOISIR :")
    print("1. generer un mot de passe")
    print("2. entrer un mot de passe")
    while True:
        choix = input("Entrer votre choix : ")
        if choix == "1":
            mdp = generer_mdp()
            break
        elif choix == "2":
            mdp = input("Entrer votre mot de passe : ")
            break
        print("saisie non valide")

    print("*VEUILLEZ SELECTIONNER UNE CATEGORIE*")
    for i, cat in enumerate(categories, 1):
        print(f"{i}. {cat}")
    print()
    try:
        choix = int(input("Entrer votre choix : "))
        if 1 <= choix <= len(categories):
            categorie = categories[choix - 1]
        else:
            print("Choix invalide, catégorie 'Autre' par défaut.")
            categorie = "Autre"
    except ValueError:
        print("Entrée invalide, catégorie 'Autre' par défaut.")
        categorie = "Autre"
    compte = input("Entrer le nom du compte : ")
    site = input("Entrer le nom du site : ")
    date_creation = datetime.now()
    # Calculer le score immédiatement pour la cohérence
    score, niveau = analyser_force(mdp)
    cles_numeriques = [int(k) for k in mot_de_passes.keys() if k.isdigit()]
    nouvelle_cle = str(max(cles_numeriques, default=0) + 1)
    mot_de_passes[nouvelle_cle] = {
        "Categorie": categorie,
        "Compte": compte,
        "Site": site,
        "Mot de passe": mdp,
        "Date": date_creation,
        "Score": score
    }
    print("________votre compte a bien été ajouté_______")


def lister_comptes():
    """
    fonction qui fait la liste des comptes
    :return: None
    """
    print("*********LISTE DES COMPTES*********")
    if len(mot_de_passes) == 0:
        print()
        print()
        print("______la liste est vide________")
        print("Aucun compte n'a encore été enrregistré")
    else:
        for cle, val in mot_de_passes.items():
            print()
            print("Compte : ", cle)
            print()
            for cle1, val1 in val.items():
                print(cle1, ":", val1)


def rechercher():
    """
    fonction qui recherche dans la base de donnees
    :return: None
    """
    print("\n******* QUE VOULEZ-VOUS RECHERCHER ? *******")
    print("1. Rechercher par catégorie")
    print("2. Rechercher par nom de site")
    choix = input("Votre choix : ")
    trouve = False
    recherche = input("Entrer votre recherche : ").strip().lower()
    print("\n___________ Résultat de la Recherche _________")
    for val in mot_de_passes.values():
        # Utilisation de la clé "Categorie" sans accent pour correspondre à ajouter_compte
        valeur_a_comparer = ""
        if choix == "1":
            valeur_a_comparer = val["Categorie"].lower()
        elif choix == "2":
            valeur_a_comparer = val["Site"].lower()
        if recherche in valeur_a_comparer:
            for key, value in val.items():
                print(f"{key} : {value}")
            print("-" * 20)
            trouve = True
    if not trouve:
        print("Aucun résultat trouvé.")


def calculer_stats():
    """
    Fonction qui calculer les stats du compte
    :return: None
    """
    total_comptes = len(mot_de_passes)
    if total_comptes == 0:
        print("\nAucune donnée disponible pour les statistiques.")
        return
    somme_scores = 0
    # On nettoie les espaces dans les catégories pour éviter les erreurs (" Autre" -> "Autre")
    stats_cat = {cat.strip(): 0 for cat in categories}
    mdp_faibles = []
    mdp_anciens = []
    # Pour les doublons, on compte les occurrences de chaque MDP
    tous_mdps = [val["Mot de passe"] for val in mot_de_passes.values()]
    for val in mot_de_passes.values():
        # Calcul Score Moyen
        score = val.get("Score", 0)
        somme_scores += score
        # Répartition par catégorie (avec strip() pour gérer " Autre")
        cat = val["Categorie"].strip()
        if cat in stats_cat:
            stats_cat[cat] += 1
        else:
            stats_cat["Autre"] = stats_cat.get("Autre", 0) + 1
        # Mots de passe faibles
        if score < 50:
            mdp_faibles.append(val)
        # Mots de passe anciens (> 90 jours)
        date_val = val["Date"]
        if isinstance(date_val, str):
            try:
                date_creation = datetime.fromisoformat(date_val) if "T" in date_val else datetime.strptime(date_val,"%Y-%m-%d %H:%M:%S.%f")
            except:
                date_creation = datetime.now()
        else:
            date_creation = date_val
        if (datetime.now() - date_creation).days > 90:
            mdp_anciens.append(val)
    # Détection des doublons (MDP utilisés plus d'une fois)
    mdp_doublons_liste = [m for m in tous_mdps if tous_mdps.count(m) > 1]
    # On transforme en set pour avoir la liste unique des MDP compromis
    mdp_doublons_uniques = set(mdp_doublons_liste)
    score_moyen = somme_scores / total_comptes
    print("\n" + "=" * 50)
    print(f"{'STATISTIQUES GLOBALES':^50}")
    print("=" * 50)
    print(f"Nombre total de comptes : {total_comptes}")
    print(f"Score de sécurité moyen : {score_moyen:.1f}/100")
    print("\n--- Répartition par catégorie ---")
    for cat, nb in stats_cat.items():
        if nb > 0:
            pourcentage = (nb * 100) / total_comptes
            print(f"{cat:<15} : {nb} ({pourcentage:.1f}%)")
    print("\n--- ALERTES SÉCURITÉ ---")
    print(f"Faibles (<50)  : {len(mdp_faibles)}")
    print(f"Anciens (>90j) : {len(mdp_anciens)}")
    print(f"En double      : {len(mdp_doublons_uniques)} mot(s) de passe utilisé(s) plusieurs fois")
    if mdp_faibles or mdp_anciens:
        print("\n--- Actions recommandées ---")
        for item in mdp_faibles:
            print(f" • Changer MDP de : {item['Site']} (Trop faible: {item['Score']})")


def sauvegarder():
    """
    fonction qui sauvegarde dans le fichier JSON
    :return: None
    """
    try:
        # Convertir les objets datetime en chaînes pour JSON
        comptes_a_sauver = {}
        for k, v in mot_de_passes.items():
            v_copy = v.copy()
            if isinstance(v_copy["Date"], datetime):
                v_copy["Date"] = v_copy["Date"].strftime("%Y-%m-%d %H:%M:%S.%f")
            comptes_a_sauver[k] = v_copy
        with open("passwords.json", "w", encoding="utf-8") as fichier:
            json.dump(comptes_a_sauver, fichier, indent=4)
        print("Fichier sauvegardé avec succès dans 'passwords.json' !")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde : {e}")

def charger_donnees():
    """
    fonction qui charge les comptes depuis le fichier JSON s'il existe, sinon initialise une base vide
    :return: None
    """
    global mot_de_passes
    try:
        with open("passwords.json", "r", encoding="utf-8") as fichier:
            data = json.load(fichier)
            if isinstance(data, dict):
                mot_de_passes = data
            else:
                mot_de_passes = {}
        # Conversion des dates
        for val in mot_de_passes.values():
            if isinstance(val.get("Date"), str):
                try:
                    val["Date"] = datetime.strptime(val["Date"], "%Y-%m-%d %H:%M:%S.%f")
                except ValueError:
                    val["Date"] = datetime.now()
        print("Données chargées avec succès.")
    except FileNotFoundError:
        mot_de_passes = {}
        print("Aucun fichier trouvé, base initialisée.")
    except json.JSONDecodeError:
        mot_de_passes = {}
        print("Fichier JSON invalide, base réinitialisée.")



def menu():
    """
    fonction qui affiche le menu et lance les fonctions
    :return: None
    """
    while True:
        print("\n========== GESTIONNAIRE DE MOTS DE PASSE ==========")
        print("1. Générer un mot de passe")
        print("2. Analyser la force d’un mot de passe")
        print("3. Ajouter un compte")
        print("4. Lister les comptes")
        print("5. Rechercher un compte")
        print("6. Calculer les statistiques")
        print("7. Sauvegarder les comptes")
        print("0. Quitter")
        print("==================================================")
        choix = input("Votre choix : ")
        if choix == "1":
            print(generer_mdp())
        elif choix == "2":
            mdp = input("Entrez le mot de passe à analyser : ")
            score, niveau = analyser_force(mdp)
            print(f"Score : {score}/100 — Niveau : {niveau}")
        elif choix == "3":
            ajouter_compte()
        elif choix == "4":
            lister_comptes()
        elif choix == "5":
            rechercher()
        elif choix == "6":
            calculer_stats()
        elif choix == "7":
            sauvegarder()
        elif choix == "0":
            print("Au revoir ")
            break
        else:
            print("Choix invalide, veuillez réessayer.")

charger_donnees()
menu()
