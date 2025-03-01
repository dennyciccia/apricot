from classes.costanti import *


class Piatto:
    def __init__(self, nome, portata, base, ingredienti=None, ricetta="", consiglio_contorno=None):
        if portata in PORTATE:
            self.__portata = portata
        else:
            raise AttributeError(f"La portata non è un valore tra [{", ".join(PORTATE)}].")

        if base in BASI:
            self.__base = base
        else:
            raise AttributeError(f"La base non è un valore tra [{", ".join(BASI)}].")
        
        self.__nome = nome
        self.__ingredienti = ingredienti
        self.__ricetta = ricetta
        self.__consiglio_contorno = consiglio_contorno


    @property
    def nome(self):
        return self.__nome


    @nome.setter
    def nome(self, value):
        self.__nome = value


    @property
    def portata(self):
        return self.__portata


    @portata.setter
    def portata(self, value):
        self.__portata = value


    @property
    def base(self):
        return self.__base


    @base.setter
    def base(self, value):
        self.__base = value


    @property
    def ingredienti(self):
        return self.__ingredienti


    @ingredienti.setter
    def ingredienti(self, value):
        self.__ingredienti = value


    @property
    def ricetta(self):
        return self.__ricetta


    @ricetta.setter
    def ricetta(self, value):
        self.__ricetta = value


    @property
    def consiglio_contorno(self):
        return self.__consiglio_contorno


    @consiglio_contorno.setter
    def consiglio_contorno(self, value):
        self.__consiglio_contorno = value


    def debug_print(self):
        print(f"nome: {self.nome}")
        print(f"base: {self.base}")
        print(f"ingredienti:")
        for i in self.ingredienti:
            print(f"\t-{i}")
        print(f"ricetta: {self.ricetta}")
        print(f"consiglio contorno:")
        for i in self.consiglio_contorno:
            print(f"\t-{i}")
