def test(test, original):
    """
    Compare une liste de caractères 'test' à une liste de caractères 'original' et renvoie une chaîne de caractères
    représentant les indications du nombre de caractères présents à la même place ('N'), 
    les caractères présents mais à la mauvaise place ('B') et les caractères absents ('X').

    ENTREE:
        test (list): la combinaison à tester.
        original (list): la combinaison à laquelle 'test' est comparé.

    SORTIE:
        str: une chaîne de caractères contenant les indications sur les couleurs présentes à la même place ('N'), 
        les couleurs présentes mais à la mauvaise place ('B') et les couleurs absentes ('X').

    EXEMPLE:
        entrée : test(['1', '2', '3', '4'], ['4', '5', '6', '8'])
        sortie : XXXB
    """
    reponse = "" # definition de la variable "reponse", qui contiendra les indications
    for i in range(len(test)): # 
        if test[i] == original[i]: # Si présent à la même place, on ajoute N à l'indication
            reponse += "N"
        elif test[i] in original:
            reponse += "B" # Si présent mais à la mauvaise place, on ajoute B à l'indication
        else:
            reponse += "X" # Si absent de la combinaison, on ajoute un X.
    return reponse

if __name__ == "__main__": # seulement si on lance directement le script
    # On compare le résultat attendu avec celui obtenu pour tester la fonction
    if test(['1', '2', '3', '4'], ['4', '5', '6', '8']) == "XXXB":
        print("Test réussi")
    else:
        print("Test échoué")

    if test(['1', '2', '3', '4'], ['1', '2', '3', '4']) == "NNNN":
        print("Test réussi")
    else:
        print("Test échoué")

    if test(['1', '2', '3', '4'], ['5', '6', '7', '8']) == "XXXX":
        print("Test réussi")
    else:
        print("Test échoué")

    if test(['1', '2', '3', '4'], ['1', '3', '2', '4']) == "NBBN":
        print("Test réussi")
    else:
        print("Test échoué")