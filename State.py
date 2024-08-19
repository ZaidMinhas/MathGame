class State:
	def __init__(self):
		self.transition = {}		
		
	def display(self):
		print('\033c', end = '', flush = True)
	
	def getInput(self):
		while True:
			inp = input(":")
			if inp in self.transition.keys():
				return self.transition[inp]
	
	def __call__(self):
		
		self.display()
		current_state = self.getInput()
		
		return current_state()