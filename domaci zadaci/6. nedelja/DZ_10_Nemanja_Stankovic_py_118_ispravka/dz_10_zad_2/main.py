
from discipline import Discipline

def main():

    sprint_100m=Discipline("sprint_100m","RUNNING",2)
    sprint_100m.input_data()
    print(sprint_100m.best_athlete())
    LongJump=Discipline("long_jump","JUMPING",3)
    LongJump.input_data()
    print(LongJump.best_athlete())

if __name__ == '__main__':
    main()



