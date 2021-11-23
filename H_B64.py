import random
import string
import os
import base64
from base64 import *
from base64 import encode, decode, b64encode, b64decode
from random import choice, randint
from art import *
from termcolor import colored

def main():
    
    #ascii art 
    print(colored(text2art ("\t________________"),'green'))
    print(colored(text2art ("\t_Hacheur_Base64_"),'green'))
    print(colored(text2art ("\t________________\n"),'green'))                      

    try:
        print("="*95)
        print("/tbonjour, que voulez vous faire ? (Encodé/Decodé) :")
        choice = input("\t> ")

        if choice == 'E':
            encode_message =input("Entré le texte a encodé: >")
            encoder = base64.encode(encode_message)
            print("[+] En Cours d'Encodage.....\n")
            print("Encodage Terminé !\n")
            print(encoder)
            
            main()
        
        elif choice == 'D':
            decode_message =input("Entré le texte a décodé: >")
            decoder = base64.b64decode(decode_message)
            print("[+] En Cours de Décodage.....\n")
            print("Décodage Terminé !\n")
            print(decoder)

            main()
        
        print("\tVoulez vous Retourné à l'acceuil ? (y/n)")
        choice = input("\t> ")

        if choice == 'y':
            main()
        
        elif choice == 'n':
            print("\t[!] Au Revoir !!")


    except KeyboardInterrupt:
        print("\n\t[!] Vous avez appuyé sur ctrl + C pour quitter instantanément")

main()
