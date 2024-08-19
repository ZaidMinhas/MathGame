from GameStates import MainMenu

def main():
	current_state = MainMenu()
	while True:
		current_state = current_state()

if __name__ == "__main__":
	main()