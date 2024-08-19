import random
from dataclasses import dataclass, field
from typing import Callable, ClassVar, List, Tuple

@dataclass
class Level:
	Levels: ClassVar[List['Level']] = []
	
	name: str
	a: Tuple[int, int]
	b: Tuple[int, int]
	sym: str
	op: Callable
    
	def __post_init__(self):
		self.Levels.append(self)
		
	def generate(self):
		a,b = self._generate()

		exp = f"{a} {self.sym} {b} = "
		sol = self.op(a,b)

		return exp, sol

	def _generate(self):
		a = random.randint(*self.a)
		b = random.randint(*self.b)

		return a,b
		

class SubLevel(Level):
	def _generate(self):
		a,b = super()._generate()
		return max(a, b), min(a, b)

class DivLevel(Level):
	def _generate(self):
		a,b = super()._generate()
		c = a*b
		return c,b


Level("Addition I", (0,50), (0,50), '+', int.__add__)
Level("Addition II", (0,100), (0,100), '+', int.__add__)

SubLevel("Subtraction I",(0,50), (0,50), '-', int.__sub__)
SubLevel("Subtraction II", (0,100), (0,100), '-', int.__sub__)

Level("Add Sub III", (-100,100), (-100,100), '+', int.__add__)

Level("Multiplication I", (0,10), (0,10), '+', int.__mul__)
Level("Multiplication II", (0,100), (0,10), '+', int.__mul__)

DivLevel("Division I", (1,10), (1,10), '/', int.__floordiv__)
DivLevel("Division II", (1,100), (1,10), '/', int.__floordiv__)