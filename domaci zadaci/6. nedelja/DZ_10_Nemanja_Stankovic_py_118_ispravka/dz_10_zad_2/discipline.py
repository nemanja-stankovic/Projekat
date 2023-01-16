from enum import Enum
from jumper import Jumper
from runner import Runner


class Discipline:

    def __init__(self,discipline_name:str,type:str,number_of_competitors:int):
        self.__discipline_name=discipline_name
        self.__type=type
        self.__number_of_competitors=number_of_competitors

    def get_discipline_name(self):
        return self.__discipline_name

    def get_type(self):
        return self.__type

    def get_number_of_competitors(self):
        return self.__number_of_competitors

    def get_competitors(self):
        return self.__competitors

    def input_data(self):
        if self.get_type()=="RUNNING":

            list_of_runners=[]
            for i in range(self.get_number_of_competitors()):
                runner=Runner()
                runner.input_data()
                list_of_runners.append(runner)
            self.__competitors = list_of_runners
        if self.get_type()=="JUMPING":

            list_of_jumpers=[]
            for i in range(self.get_number_of_competitors()):
                jumper=Jumper()
                jumper.input_data()
                list_of_jumpers.append(jumper)
            self.__competitors = list_of_jumpers

    def best_athlete(self):
        winner_score = self.get_competitors()[0].get_score()
        winner_index = 0
        list_of_winners=[]
        for i in range(len(self.get_competitors())):
            for j in range(len(self.get_competitors())):
                if self.get_competitors()[j].is_it_better_than(self.get_competitors()[i]) and j>i:
                    winner_score=self.get_competitors()[j].get_score()
                    winner_index = j
        winner = self.get_competitors()[winner_index]
        for i in range(len(self.get_competitors())):
            if self.get_competitors()[i].get_score()==winner_score:
                list_of_winners.append(self.get_competitors()[i])
        return list_of_winners

    def __repr__(self):
        return(f"Disciplina {self.get_discipline_name()} tipa {self.get_type()}, broj takmicara: {self.get_number_of_competitors()}\ntakmicari:{self.get_competitors()}")