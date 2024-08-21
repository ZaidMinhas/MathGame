class State:
	def __init__(self):
		#Concrete classes will have their own transitions
		self.transition = {}		
		
	def display(self):
		#super will clear screen
		print('\033c', end = '', flush = True)
	
	def getInput(self):
		#gets a valid input for FSM
		while True:
			inp = input(":")
			if inp in self.transition.keys():
				return self.transition[inp]

	def __call__(self):
		self.display()
		current_state = self.getInput()
		return current_state()