import os
import keyboard
import time
from colorama import Back, Fore, Style, deinit, init
import json
from datetime import date
from pathlib import Path


def clear():
    os.system("cls")


def save_data(nom, donnees, jour):
    with open("stockage.json", "r") as f:
        data = json.load(f)
        data[nom] = {
            "MMR" : donnees,
            "date" : str(jour)
        }
        with open("stockage.json", "w") as f:
            json.dump(data, f)


def load_data():
    with open("stockage.json", "r") as f:
        data = json.load(f)
        return data


def tracker():
    clear()
    try:
        MMR_avant = int(input("MMR avant session --> "))
    except ValueError as Erreur_de_fou_malade:
        print(Erreur_de_fou_malade)
        print("Le script va se relancer seul ...")
        time.sleep(2)
        clear()
        tracker()
    clear()
    print("Session en cours ... \n")
    attente = str(input("Session finie ? (réponse : oui) --> "))
    if attente == "oui":
        clear()
        try:
            MMR_apres = int(input("MMR après session --> "))
        except ValueError as Erreur_de_fou_malade:
            print(Erreur_de_fou_malade)
            print("Tu sais pas écrire")
            time.sleep(1)
            clear()
            MMR_apres = int(input("MMR après session --> "))
            
        clear()

        result = MMR_apres - MMR_avant
        aujourdhui = date.today()
        nom = str(input("Entre le nom de ta session --> "))
        save_data(str(nom), result, aujourdhui)

        if result > 0:
            result = (Fore.GREEN + "+" + str(result) + Style.RESET_ALL)
            print(f"Résumé de session : {result} MMR")
        elif result < 0:
            result = (Fore.RED + str(result) + Style.RESET_ALL)
            print(f"Résumé de session : {result} MMR")
        elif result == 0:
            print("Session NULLE !")


    else:
        print("choix invalide")
        time.sleep(2)
        print("Le script va se relancer seul ...")
        clear()
        tracker()

def départ():
    clear()
    choix = str(input("Tracker ou voir les logs ? (T/L) --> "))
    if choix == "T":
        clear()
        tracker()
    elif choix == "L":
        clear()
        logs = load_data()
        print(json.dumps(logs, indent=4))
        input("Appuie sur une touche pour fermer\n--> ")
    else:
        print("choix invalide, le script va se relancer")
        time.sleep(2)
        départ()


fichier = Path("stockage.json")
if fichier.exists():
    départ()
else:
    first_data = {}
    with open("stockage.json", "w") as f:
        json.dump(first_data, f)
    départ()