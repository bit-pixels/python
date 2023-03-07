import random as r

while True: # This allows for a replay without restarting
    choices = ["rock", "paper", "scissors"]
    ai = r.choice(choices) # I have opted for r.choice instead of r.randint as it allows the user input to be 
    player = None

    while player not in choices:
        player = input("Rock, Paper or Scissors?: ").lower()

    print("Ai chose: " + ai.capitalize())
    print("You chose: " + player.capitalize())
    if ai == player:
        print("Draw!🪢")
    elif ai == "rock" and player == "scissors":
        print("You lost!❌")
    elif ai == "paper" and player == "rock":
        print("You lost!❌")
    elif ai == "scissors" and player == "paper":
        print("You lost!❌")
    elif ai == "rock" and player == "paper":
        print("You won!✅")
    elif ai == "paper" and player == "scissors":
        print("You won!✅")
    elif ai == "scissors" and player == "rock":
        print("You won!✅")
