import random

rules = {"rock": "scissors", "scissors": "paper", "paper": "rock"}

def getComputerChoice():
    return random.choice(list(rules.keys()))

def determineWinner(playerChoice, computerChoice):
    if playerChoice == computerChoice:
        return "draw"
    elif rules[playerChoice] == computerChoice:
        return "player"
    return "computer"


playerScore = 0
computerScore = 0

while True:
    playerChoice = input(
        "Choose (rock, scissors, paper) or 'end' to finish the game: "
    ).lower()
    if playerChoice == "end":
        break
    if playerChoice not in rules:
        print("Invalid choice. Please try again.")
        continue

    computerChoice = getComputerChoice()
    print(f"The computer chose: {computerChoice}")

    winner = determineWinner(playerChoice, computerChoice)
    if winner == "player":
        print("You won this round!")
        playerScore += 1
    elif winner == "computer":
        print("The computer won this round!")
        computerScore += 1
    else:
        print("This round is a draw.")

    print(f"Score: Player {playerScore} - Computer {computerScore}")

print("The game is over.")
print(f"Final score: Player {playerScore} - Computer {computerScore}")
