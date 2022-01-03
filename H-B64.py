import os
from os import *

system("pip install termcolor")
system("pip install art")
system("pip install random")
system("pip install string")
system("pip install base64")
system("pip install ")
system("cls")

import random
import string
import base64
from base64 import b64encode, b64decode
from random import choice
from art import *
from termcolor import colored

def main():
    
    #ascii art 
    print(colored(text2art ("\t________________"),'green'))
    print(colored(text2art ("\t______H-B64_____"),'green'))
    print(colored(text2art ("\t________________\n"),'green'))                      

    try:
        print("="*95)
        print("H-B64:$> Bonjour, que voulez vous faire ? (Encodé/Decodé) :\n")
        choice = input("H-B64:$>")

        if choice == 'E':
            encode_message =input("H-B64:$> Entré le texte a encodé:>")
            encoder = encode_message.encode("ascii")
            encode_bytes = base64.b64encode(encoder)
            encode_string = encode_bytes.decode("ascii")
            print("H-B64:$> [+] En Cours d'Encodage.....")
            print("H-B64:$> Encodage Terminé !\n")
            print("H-B64:$> le texte ", (encode_message), " donne en encodé ", (encode_string))
        
        elif choice == 'D':
            decode_message =input("H-B64:$> Entré le texte a décodé:>")
            decoder = decode_message.encode("ascii")
            decode_bytes = base64.b64decode(decoder)
            decode_string = decode_bytes.decode("ascii")
            print("H-B64:$> [+] En Cours de Décodage.....")
            print("H-B64:$> Décodage Terminé !\n")
            print("H-B64:$> le hash", (decode_message), " donne en décrypté", (decode_string))
        
        print("H-B64:$> Voulez vous Retourné à l'acceuil ? (y/n)")
        choice = input("\t> ")

        if choice == 'y':
            main()
        
        elif choice == 'n':
            print("H-B64:$> [!] Au Revoir !!")


    except KeyboardInterrupt:
        print("H-B64:$> [!] Vous avez appuyé sur ctrl + C pour quitter instantanément !!")

main()
