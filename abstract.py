from abc import ABC, abstractmethod
class Vickylife(ABC):

    @abstractmethod
    def stockmarket(self):
        pass
    @abstractmethod
    def abroaddream(self):
        pass
    @abstractmethod
    def fitness(self):
        pass

class write(Vickylife):
    def stockmarket(self):
        print("I started my profit journey")
    def abroaddream(self):
        print("I started my programming journey")
    def fitness(self):
        print("I started my fitness journey")
    def Entreprenurent(self):
        print("I yet to start my entreprenurent journey")

w=write()
w.stockmarket()
w.abroaddream()
w.fitness()
w.Entreprenurent()
