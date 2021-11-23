import base64
from base64 import standard_b64decode, standard_b64encode
from random import choice
from art import *
from termcolor import colored

def main():
    
    #ascii art 
    print(colored(text2art ("\t________________"),'green'))
    print(colored(text2art ("\t_Hacheur_Base64_"),'green'))
    print(colored(text2art ("\t________________\n"),'green'))                      

    try:
        print("="*95)
        print("Hacheur_Base64:$> Bonjour, que voulez vous faire ? (Encodé/Decodé) :\n")
        choice = input("Hacheur_Base64:$>")

        if choice == 'E':
            encode_message =input("Hacheur_Base64:$> Entré le texte a encodé:>")
            encoder = base64.standard_b64encode(encode_message)
            print("Hacheur_Base64:$> [+] En Cours d'Encodage.....\n")
            print("Hacheur_Base64:$> Encodage Terminé !\n")
            print(encoder)
            
            main()
        
        elif choice == 'D':
            decode_message =input("Hacheur_Base64:$> Entré le texte a décodé:>")
            decoder = base64.standard_b64decode(decode_message)
            print("Hacheur_Base64:$> [+] En Cours de Décodage.....\n")
            print("Hacheur_Base64:$> Décodage Terminé !\n")
            print(decoder)

            main()
        
        print("Hacheur_Base64:$> Voulez vous Retourné à l'acceuil ? (y/n)")
        choice = input("\t> ")

        if choice == 'y':
            main()
        
        elif choice == 'n':
            print("Hacheur_Base64:$> [!] Au Revoir !!")


    except KeyboardInterrupt:
        print("Hacheur_Base64:$> [!] Vous avez appuyé sur ctrl + C pour quitter instantanément !!")

main()
