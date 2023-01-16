from athlete import Athlete

class Jumper(Athlete):

    def is_it_better_than(self,other):
        if self.get_score() > other.get_score():
            return True
        else:
            return False

    def __repr__(self):
        return(f"<<Skakac {self.name} {self.surname} sa rezultatom {self.get_score()}>>")
