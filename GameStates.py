from State import State
from Level import Level

class MainMenu(State):
    def __init__(self):
        super().__init__()
        self.transition = {"1": PlayGame(), "2": Stats(), "Q": Exit(), "q": Exit()}
        
    def display(self):
        super().display()
        print("1. Play Game")
        print("2. See Stats")
        print("Q. Exit game")

class Stats(State):
	pass

class Exit(State):
	def display(self):
		super().display()
		print("Thank you for playing!")

	def __call__(self):
		self.display()
		return quit()
	
class PlayGame(State):	
	def __init__(self):
		self.transition = {"Q" : MainMenu, "q" : MainMenu}	

	def display(self):
		super().display()
		for n,lvl in enumerate(Level.Levels):
			if (n+1) %5 == 0:
				print()
			print(f"{n+1}. {lvl.name}")
		print("\nQ. Back")

	def getInput(self):
		while True:
			inp = input(":")
			if inp in self.transition.keys():
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
		print('\033c', end = '', flush = True)
		for i in range(1,questions+1):
			
			print(f"Q{i}")
			expr, sol = lvl.generate()
			_sol = input("  " + expr)
			if _sol == (sol := str(sol)):
				correct += 1
				print("CORRECT")
			else:
				print("INCORRECT, correct answer: " + sol )
		
		print(f"\nYOU GOT {correct}/{questions} CORRECT!")
		


