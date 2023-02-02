def init(combinaison):
    '''
    Prends une chaine de caractère avec les 4 couleurs dans l'ordre et la transforme en combinaison de départ sous forme de liste. 
    
    ENTREE : 
    combinaison : str : la combinaison à transformer en liste
    
    SORTIE :
    combinaison : list : la liste initiale à comparer à chaque fois
    
    Exemple : Entrée : 1938 Return : [1, 9, 3, 8]
    '''
    supportedCharacters = [1,2,3,4,5,6,7,8] # liste des caractères possibles
    combinaison = list(combinaison) # convertion de la combinaison en liste
    if len(combinaison) > 4: # Vérifie que la combinaison fait la bonne taille
        return "Erreur : Veuillez rentrer une combinaison valide !"
    for i in combinaison:
        if int(i) not in supportedCharacters: # Vérifie que les caractères de l'entrée "combinaison" sont valides
            return "Erreur : Veuillez rentrer une combinaison valide !"
    return combinaison # Retourne la combinaison de base

if __name__ == "__main__": # seulement si on lance directement le script
    valides = 0 # on définit cette variable pour plus tard.
    for i in range(10000): # On fait une boucle for pour les 10000 premiers nombres (0 compté)
        if len(init(str(i))) == 4:
            valides = valides + 1 # On incrémente la variable "valides" d'un à chaque fois qu'une valeur est valide
        print(init(str(i))) # On affiche le résultat de la fonction, pour tester.
    print("Dans cette fonction,", valides, "combinaisons sont valides") # On donne le nombre de combinaisons valides, des fois qu'on veuille vérifier par le calcul
    
