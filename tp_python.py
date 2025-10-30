#Tp
from abc import ABC, abstractmethod
from enum import Enum

class Document(ABC):
    nb_document = 0
    def __init__(self,anneepublication:int, titre:str):
        self._anneePublication = anneepublication
        self._titre = titre
        Document.nb_document += 1

    @property
    def titre(self):
        return self._titre
    @property
    def  anneepublication(self):
        return self._anneepublication
    
    @abstractmethod
    def afficherinfos(self):
        pass
    
    @classmethod
    def affichernbdocument(cls):
        print(f"Le nombre de document est {cls.nb_document}")

class Genre(Enum):
    ROMAN = "roman"
    SCIENCE_FICTION = "science fiction"
    FANTASTIQUE = "fantastique"

class Empruntable(ABC):
    def __init__(self):
        self.estemprunte = False
    
    @abstractmethod
    def emprunter(self):
        pass
    
    @abstractmethod
    def rendre(self):
        pass


class Consultable(ABC):
    @abstractmethod
    def consultable(self):
        print("Vous consultez ce document")

class DocumentDejaEmprunte(Exception):
    pass


class DocumentNonEmprunte(Exception):
    pass


class Livre(Document, Empruntable, Consultable):
    def __init__(self,titre, auteur:str, nbpages:int,genre:Genre, anneepublication):
        Document.__init__(titre, anneepublication)
        Empruntable.__init__(self)
        self.auteur = auteur
        self.genre = genre
        self.nbpages = nbpages

    @staticmethod
    def constructeur_secondaire(titre, auteur, genre):
        return Document(titre, auteur, 100, genre, 0)

    @staticmethod
    def compteurpages(list_livre):
        total = 0
        for livre in list_livre:
            total += livre.nbpages
        return total
    
    def emprunter(self):
        if self.estemprunte:
            raise DocumentDejaEmprunte(f"Le livre {self.titre} est deja emprinter")
        self.estemprunte = True
        print(f"Vous avez emprunter le livre {self.titre}.")
    
    def rendre(self):
        if not self.estemprunte:
            raise DocumentNonEmprunte(f"Le document {self.titre} n'etait pas emprunté")

    def consulter(self):
        print(f"Vous consulter ce document {self.titre} .")
    

class Magazine(Document, Consultable):
    def __init__(self,titre, numero:int, annepublication):
        super().__init__(titre, annepublication)
        self.numero = numero


    def consulter(self):
        print(f"Vous consulter le magazine {self.titre}" )


# def afficher_infos(self):
#     print(f"Titre : {self.titre}")
# bibliotheque = ["livre", "livre1", "livre2"]
# print(Livre.afficherinfos(bibliotheque))


            







