from Level import Level

class PlayGame:
	def __init__(self):
		super().__init__()
		self.display()
		
	def display(self):
		for n,lvl in enumerate(Level.Levels):
			if (n+1) %5 == 0:
				print()
			print(f"{n+1}. {lvl.name}")
		print("\nQ. Back")

		selected_lvl = self.getInput()
		print(selected_lvl.name)
		self.play(selected_lvl)

	def getInput(self):
		self.right, self.wrong = 0,0
		self.check = []
		while True:
			try:
				inp = input(":")
				if inp == "Q":
					exit()
					break
				else:
					lvl = Level.Levels[int(inp)-1]
					return lvl
			except (ValueError, IndexError):
				pass

	def play(self, lvl : Level):
		correct, questions  = 0,10
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

