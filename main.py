from essai import essai
from init import init
from test import test
import colorama
from colorama import Fore # Pour définir des couleurs

# Message d'accueil
print("Bienvenue sur le MasterMind ! \n\n")
print(Fore.BLUE + '[1] - Bleu\n')
print(Fore.RED + '[2] - Rouge\n')
print(Fore.GREEN + '[3] - Vert\n')
print(Fore.YELLOW + '[4] - Jaune\n')
print('[5] - Orange\n')
print(Fore.MAGENTA + '[6] - Rose\n')
print('[7] - Violet')
print(Fore.RESET)
print('[8] - Marron\n')


while True: # On fait une boucle pour redemander la combinaison à l'utilisateur tant que celle-ci n'est pas valide.
    codeInitial = init(input(Fore.BLUE + "[JOUEUR 1] - Entrez la combinaison de quatre couleurs à deviner, selon le code ci-dessus : ")) # Définition de la combinaison initiale
    #Vérification de la combinaison de l'utilisateur, sinon affichage de l'erreur
    if len(codeInitial) == 4:
        print("\n")
        break
    else:
        print(Fore.RED + codeInitial)

for i in range(10):
    while True: # On fait une boucle pour redemander la combinaison à l'utilisateur tant que celle-ci n'est pas valide.
        codeTest = essai(input(Fore.BLUE + "[JOUEUR 2] - Entrez la combinaison de quatre couleurs à tester, selon le code défini plus haut : ")) # Définition de la combinaison à test
        # Vérification de la combinaison de l'utilisateur, sinon affichage de l'erreur
        if len(codeTest) == 4:
            break
        else:
            print(Fore.RED + codeTest)
    # Affichage du résultat
    print(Fore.BLUE + "\n[ORDINATEUR] - Indications sur le code : " + test(codeTest, codeInitial) + "\n")
    if test(codeTest, codeInitial) == "NNNN":
        print(Fore.GREEN + "[ORDINATEUR] - Code correct, le joueur 2 remporte la partie !")
        break
    # Vérification du nombre d'essai
    if i == 9:
        print(Fore.GREEN + "[ORDINATEUR] - Nombre de tentative max. atteint, le joueur 1 remporte la partie !")
        break