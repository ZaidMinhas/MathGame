from State import State
from Level import Level
from ProgressBar import ProgressBar
import Stats

class MainMenu(State):
    def __init__(self):
        super().__init__()
        self.transition = {"1": PlayGame, "2": StatsMenu, "Q": Exit, "q": Exit}
        
    def display(self):
        super().display()
        print("Welcome to the Math Game, by Zaid")
        print("1. Play Game")
        print("2. See Stats")
        print("Q. Exit game")

class StatsMenu(State):
    def __init__(self):
        super().__init__()
        self.transition = {"Q": MainMenu, "q": MainMenu}

    def display(self):
        super().display()
        stats_dict = Stats.readStats()
        for sym in stats_dict:
            print(stats_dict[sym][2])
            print("  " + Stats.getProgressBar(sym))
        print("\nQ. Back")
        


class PlayGame(State):	
    def __init__(self):
        super().__init__()
        self.transition = {"Q" : MainMenu, "q" : MainMenu}	

    def display(self):
        super().display()
        for n,lvl in enumerate(Level.Levels):
            if (n+1) %4 == 0:
                print()
            print(f"{n+1}. {lvl.name}")
        print("\nQ. Back")

    def getInput(self):
        while True:
            inp = input(":")
            if inp in self.transition:
                return self.transition[inp]
            else:
                try:
                    lvl = Level.Levels[int(inp)-1]
                    self.play(lvl)
                    self.display()
                except (ValueError, IndexError):
                    pass

    def play(self, lvl : Level):
        self.right, self.wrong = 0,0
        self.check = []
        correct, questions  = 0,10
        pb = ProgressBar(10)
        print('\033c', end = '', flush = True)
        for i in range(1,questions+1):
            print(f"Q{i}/{questions}")

            expr, sol = lvl.generate()
            _sol = input("  " + expr)
            output = _sol == (sol := str(sol))
            if output:
                correct += 1
                print("CORRECT")
            else:
                print("INCORRECT, correct answer: " + sol )
            print(pb(i/questions))
            inp = input(":")
            if inp in self.transition:
                return self.transition[inp]

            print('\033c', end = '', flush = True)
        
        print(f"\nYOU GOT {correct}/{questions} CORRECT!")
        Stats.updateScore(lvl.sym, correct*lvl.points)
        print(Stats.getProgressBar(lvl.sym))
        input("")
        

class Exit(State):
    def display(self):
        super().display()
        print("Thank you for playing!")

    def __call__(self):
        self.display()
        return quit()
    