from classes.piatto import Piatto
from classes.lista_piatti import ListaPiatti
from classes.costanti import *

def menu():
    print("Seleziona una funzione:")
    print("1. Piatto a caso data una base")
    print("2. Piatto a caso data una base e degli ingredienti")
    print("3. Tutti i piatti data una base")
    print("4. Tutti i piatti data una base e degli ingredienti")
    print("0. Chiudi il programma")
    scelta = input("Scelta: ")
    return scelta

def chiedi_ingredienti():
    ingredienti = input("Scrivi gli ingredienti separati da una virgola: ")
    lista_ingredienti = ingredienti.split(",")
    return lista_ingredienti

def chiedi_portata():
    ok = False
    while not ok:
        portata = input("Scrivi la portata: ")
        if portata in PORTATE:
            ok = True
    return portata

def chiedi_base():
    ok = False
    while not ok:
        base = input("Scrivi la base: ")
        if base in BASI:
            ok = True
    return base

def print_risultato_ricerca(result):
    print()

    # print di un piatto
    if type(result) is Piatto:
        print(f"Risultato: {result.nome}")

        if result.ricetta is not None:
            print(f"Ricetta: {result.ricetta}")
        else:
            print("Ricetta: ")

        print("Consiglio contorno:")
        if result.consiglio_contorno is not None:
            for c in result.consiglio_contorno:
                print(f"\t- {c}")

    # print di una lista di piatti
    elif type(result) is ListaPiatti:
        for p in result:
            print(p.nome)

    elif result is None:
        print("Nessun piatto corrisponde ai criteri di ricerca")
    else:
        print("Errore nella chiamata della funzione")

    print()
    input("Premi invio per continuare...")
    print()