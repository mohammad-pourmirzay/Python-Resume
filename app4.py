import random

choices = ["Rock", "Paper", "Scissors"]
player = False
cpu_score = 0
player_score = 0
tie_score = 0
game = 0
while True:
    computer = random.choice(choices)
    player = input("Rock, Paper or  Scissors?").capitalize()
    if player == computer:
        print("Tie!")
        tie_score += 1
        game += 1
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            cpu_score += 1
            game += 1
        else:
            print("You win!", player, "smashes", computer)
            player_score += 1
            game += 1
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            cpu_score += 1
            game += 1
        else:
            print("You win!", player, "covers", computer)
            player_score += 1
            game += 1
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
            cpu_score += 1
            game += 1
        else:
            print("You win!", player, "cut", computer)
            player_score += 1
            game += 1
    else:
        print("That's not a valid play. Check your spelling!")
    if game == 3:
        print("Final Scores:")
        print(f"CPU:{cpu_score}")
        print(f"Plaer:{player_score}")
        print(f"Tie:{tie_score}")
        if cpu_score > player_score:
            print("CPU won and you lost")
        elif cpu_score < player_score:
            print("you won and lost CPU")
        elif cpu_score == player_score or tie_score > player_score or cpu_score:
            print("you and CPU are equal")
        print("Game Over!!!")
        while True:
            are_you_playing_again = input("Are you playing again? Yes/No: ").capitalize()
            if are_you_playing_again == "Yes":
                game = 0
                cpu_score = 0
                player_score = 0
                tie_score = 0
                print("start please")
                break
            elif are_you_playing_again == "No":
                print("good game")
                break
            else:
                print("Please select Yes or No!!")
        if are_you_playing_again == "No":
            break


