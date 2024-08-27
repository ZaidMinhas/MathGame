import random


class Level:
	Levels = []
	ops = {"+" : int.__add__, "-" : int.__sub__, "*" : int.__mul__, "^" : int.__pow__}
	
	def __init__(self, name, a,b, sym, points = 10):
		self.name = name
		self.a = a
		self.b = b
		self.sym = sym
		self.points = points
		if sym in Level.ops:
			self.op = Level.ops[sym]
		Level.Levels.append(self)
		
	
	def getExp(self,a,b):
		return f"{a} {self.sym} {b} = "
	
	def getSol(self,a,b):
		return self.op(a,b)
		

	def generate(self):
		a,b = self._generate()

		exp = self.getExp(a,b)
		
		sol = self.getSol(a,b)

		return exp, sol

	def _generate(self):
		a = random.randint(*self.a)
		b = random.randint(*self.b)

		return a,b
		

#inherited classes that change functionality of certain levels (might improve or even change to a decorator) 
class SubLevel(Level):
	def _generate(self):
		a,b = super()._generate()
		return max(a, b), min(a, b)

class DivLevel(Level):
	def getSol(self, a, b):
		return self.sol

	def _generate(self):
		a,b = super()._generate()
		c = a*b
		self.sol = a
		return c,b
	
class RootLevel(Level):
	def getSol(self, a,b):
		return self.sol

	def _generate(self):
		a,b =  super()._generate()
		c = b**a
		self.sol = b
		return a,c

class TriLevel(Level):
	def __init__(self, name, ranges, syms):
		self.name = name
		self.ranges = ranges
		self.syms = list(syms)
		self.ops = [Level.ops[i] for i in syms]

	def generate(self):
		terms = self._generate()
		random.shuffle(self.syms)
		
		expr = str(terms[0]) +" " +  " ".join([self.syms[i] + " " + str(terms[i+1]) for i in range(len(self.syms))])

		return expr, eval(expr)

	def _generate(self):
		terms = [random.randint(a,b) for (a,b) in self.ranges]
		return terms

#Creation of Levels (More to be added and improved)
Level("Addition I", (0,50), (0,50), '+', 5)
Level("Addition II", (0,100), (0,100), '+', 15)

SubLevel("Subtraction I",(0,50), (0,50), '-', 10)
SubLevel("Subtraction II", (0,100), (0,100), '-', 25)

# Level("Add Sub III", (-100,100), (-100,100), '+', )

Level("Multiplication I", (0,10), (0,10), '*', 5)
Level("Multiplication III", (0,100), (0,10), '*', 25)


DivLevel("Division I", (1,10), (1,10), '/', 5)
DivLevel("Division II", (1,100), (2,10), '/', 25)

Level("Square I", (0,10), (2,2), "^", 5)
Level("Square II", (0,100), (2,2), "^", 20)

Level("Cube I", (0,10), (3,3), "^", 5)
Level("Cube II", (0,100), (3,3), "^", 25)


RootLevel("Square Roots I", (2,2), (1,10), "√", 10)
RootLevel("Square Roots II", (2,2), (1,100), "√", 25)

RootLevel("Cube Roots I", (3,3), (1,10), "√", 15)
RootLevel("Cube Roots II", (3,3), (1,100), "√", 30)
