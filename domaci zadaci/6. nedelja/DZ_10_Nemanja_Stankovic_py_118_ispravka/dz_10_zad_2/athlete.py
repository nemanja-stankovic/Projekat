from abc import ABC,abstractmethod


class Athlete(ABC):

    def get_score(self):
        return self.__score

    def set_score(self,score):
        self.__score=score

    def input_data(self):
        self.name = input("Unesite ime atleticara:\n")
        self.surname = input("Unesite prezime atleticara:\n")
        self.__score = float(input("Unesite rezultat atleticara:\n"))

    @abstractmethod
    def is_it_better_than(self, other):
        pass





