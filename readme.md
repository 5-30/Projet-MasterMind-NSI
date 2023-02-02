
# Projet NSI : MasterMind

## Répartition des tâches :
* Fonction init :
    * Prends une chaine de caractère avec les 4 couleurs dans l'ordre et la transforme en combinaison de départ sous forme de liste. Exemple : Entrée : `1938` Return : `[1, 9, 3, 8]` -- **Clément F.**
* Fonction Essai :
   * Prends une chaine de caractère avec les 4 couleurs dans l'ordre et la transforme en combinaison à tester sous forme de liste. Exemple : Entrée : `1938` Return : `[1, 9, 3, 8]` -- **Clément F.**
* Fonction test :
   * Prends une liste avec les 4 couleurs à tester dans l'ordre et compare chacune d'entre elles à la cominaison à deviner. Noir = Bien placée, Blanc = Bonne couleur mal placée, espace = Tout faux. Exemple : Entrée : `9378` Return : `BB N` -- **Hugo**
* Programme Principal :
   * Appel de la fonction init pour définir la combinaison de départ dans une variable, puis entrée dans une boucle while qui print le résultat de la fonction Essai par la fonction test et casse la boucle si le résultat = NNNN -- **Addam**
