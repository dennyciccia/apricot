import operator
import pandas
import random
import numpy
from classes.piatto import Piatto

class ListaPiatti:
    # attributi di istanza
    # __lista -> lista dei piatti
    # __ingredienti -> set di tutti gli ingredienti presenti nei piatti

    def __init__(self, lista=None):
        if lista is not None:
            self.__lista = lista
        else:
            self.__lista = list()

        self.__ingredienti = set()

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index < len(self.__lista):
            value = self.__lista[self.__index]
            self.__index += 1
            return value
        else:
            raise StopIteration

    @property
    def ingredienti(self):
        return list(self.__ingredienti)

    def add(self, piatto):
        self.__lista.append(piatto)

    def read(self, nomefile):
        dataframe = pandas.read_excel(nomefile)

        # esamino ogni riga del dataframe
        for i in range(dataframe.index.stop):
            row = dataframe.loc[i, :]  # dizionario

            # normalizzazione dei campi (perchè una cella vuota del foglio excel viene letta come NaN(float))
            ingredienti = row["ingredienti"].split(",")

            if not isinstance(row["ricetta"], numpy.float64) and not isinstance(row["ricetta"], float):
                ricetta = row["ricetta"]
            else:
                ricetta = None

            if not isinstance(row["consiglio contorno"], numpy.float64) and not isinstance(row["consiglio contorno"], float):
                consiglio_contorno = row["consiglio contorno"].split(",")
            else:
                consiglio_contorno = None

            # costruzione piatto e inserimento nella lista dei piatti
            piatto = Piatto(row["nome"], row["portata"], row["base"], ingredienti, ricetta, consiglio_contorno)
            self.__lista.append(piatto)

            # aggiornamento lista ingredienti
            for ingr in ingredienti:
                self.__ingredienti.add(ingr)

    def piatto_a_caso(self, portata, base=None, ingredienti=None):
        lista_temp = list()

        for p in self.__lista:
            if self.__piatto_idoneo(p,portata,base,ingredienti):
                lista_temp.append(p)

        if len(lista_temp) > 0:
            piatto = random.choice(lista_temp)
        else:
            piatto = None

        return piatto

    def tutti_i_piatti(self, portata, base=None, ingredienti=None):
        piatti_conformi = ListaPiatti()

        for piatto in self.__lista:
            if self.__piatto_idoneo(piatto,portata,base,ingredienti):
                piatti_conformi.add(piatto)

        return piatti_conformi

    @staticmethod
    def elemento_comune(list1, list2):
        for elem in list2:
            if operator.countOf(list1,elem) > 0:
                return True
        return False

    def __piatto_idoneo(self, piatto, portata, base=None, ingredienti=None):
        idoneo = False

        # se è della portata richiesta allora va bene
        if piatto.portata == portata:
            idoneo = True

        # se la base è stata specificata se corrisponde
        if base is not None:
            if piatto.base != base:
                idoneo = False

        # se sono stati specificati anche gli ingredienti controlla
        # che almeno uno di quelli sia tra gli ingredienti nel piatto
        if ingredienti is not None:
            if not self.elemento_comune(piatto.ingredienti, ingredienti):
                idoneo = False

        return idoneo

    def get_ingr_number(self):
        return len(self.__ingredienti)
