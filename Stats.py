import json
from ProgressBar import ProgressBar
def init():
		score_dict = {"+" :(0,0, "Addition"), "-" : (0,0, "Subtraction"), "*" : (0,0, "Multiplication"), "/" : (0,0, "Division"), "^" : (0,0, "Power"), "√" : (0,0, "Roots")}
		writeStats(score_dict)

def readStats():
	with open('stats.json', 'r') as openfile:
		stats_dict = json.load(openfile)
	return stats_dict

def writeStats(score_dict):
	with open('stats.json', 'w') as outfile:
		json.dump(score_dict, outfile)
	

def LevelScore(level):
		return 100*int((1.5)**level)
	
def updateScore(sym, _score):
	stats_dict = readStats()

	score, level, _ = stats_dict[sym]

	score_needed = LevelScore(level)
	score += _score
	print(f"+{score} xp")
	if score > score_needed:
		score = score - score_needed
		level += 1
		print("YOU LEVELED UP")
		
	stats_dict[sym] = score, level, _

	writeStats(stats_dict)



def getSymStats(sym):
	stats_dict = readStats()
	return stats_dict[sym]
	
def getProgressBar(sym):
	score, level, _ = getSymStats(sym)
	pb = ProgressBar(50, fill = '⬜', unfill= '⬛')
	score_needed = LevelScore(level)
	return f"{level} {pb(score/score_needed)} {level+1}"



	

if __name__ == "__main__":
	init()
	getSymStats("+")
	updateScore("+", 10)
	getSymStats("+")
	print(getProgressBar("+"))