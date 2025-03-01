import operator
import pandas
import random
import numpy
from classes.piatto import Piatto

class ListaPiatti(list):
    # attributi di istanza
    # __ingredienti -> set di tutti gli ingredienti presenti nei piatti


    def __init__(self):
        super().__init__()
        self.__ingredienti = set()


    @property
    def ingredienti(self):
        return list(self.__ingredienti)


    def read_from_file(self, nomefile):
        df = pandas.read_excel(nomefile)
        df.columns = df.columns.str.replace(' ', '_')

        # esamino ogni riga del dataframe
        for row in df.itertuples()[1:]:
            ingredienti = row.ingredienti.split(",")

            if not isinstance(row.ricetta, numpy.float64) and not isinstance(row.ricetta, float):
                ricetta = row.ricetta
            else:
                ricetta = None

            if not isinstance(row.consiglio_contorno, numpy.float64) and not isinstance(row.consiglio_contorno, float):
                consiglio_contorno = row.consiglio_contorno.split(",")
            else:
                consiglio_contorno = None

            # costruzione piatto e inserimento nella lista dei piatti
            piatto = Piatto(row.nome, row.portata, row.base, ingredienti, ricetta, consiglio_contorno)
            self.append(piatto)

            # aggiornamento lista ingredienti
            for ingr in ingredienti:
                self.__ingredienti.add(ingr)


    def piatto_a_caso(self, portata, base=None, ingredienti=None):
        lista_temp = list()

        for p in self:
            if self.__piatto_idoneo(p,portata,base,ingredienti):
                lista_temp.append(p)

        if len(lista_temp) > 0:
            piatto = random.choice(lista_temp)
        else:
            piatto = None

        return piatto


    def tutti_i_piatti(self, portata, base=None, ingredienti=None):
        piatti_conformi = ListaPiatti()

        for piatto in self:
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
