import random
game_symbols = ["rock", "paper", "scissor"]
computers_choice = random.choice(game_symbols)

def last_step():
    print("thank you for participating in the game")

def game(user_input):
    if user_input == "rock" or user_input == "paper" or user_input == "scissor":
        print("please enter the spelling properly!!!!")
    elif user_input == computers_choice:
        print("its a tie!!!!!!!")
        print(f"number of chances left {4-(i+1)}")
        print(f"you entered {user_input} and computer's choice is {computers_choice}")
    elif user_input == "rock" and computers_choice == "paper":
        print("you lost!!!!!!!")
        print(f"you entered {user_input} and computer's choice is {computers_choice}") 
        print("please try again")
        print(f"number of chances left {4-(i+1)}")
    elif user_input == "rock" and computers_choice == "scissor":
        print("you won!!!!!")
        print(f"you entered {user_input} and computer's choice is {computers_choice}") 
        last_step()
    elif user_input == "paper" and computers_choice == "scissor":
        print("you lost!!!!!!!!!!!")
        print(f"you entered {user_input} and computer's choice is {computers_choice}") 
        print("please try again")
        print(f"number of chances left {4-(i+1)}")
    elif user_input == "paper" and computers_choice == "rock":
        print("you won!!!!!!!!!!!")
        print(f"you entered {user_input} and computer's choice is {computers_choice}") 
        last_step()
    elif user_input == "scissor" and computers_choice == "rock":
        print("you lost!!!!!!!!!!!")
        print(f"you entered {user_input} and computer's choice is {computers_choice}") 
        print("please try again")
        print(f"number of chances left {4-(i+1)}")
    else:
        print("you won!!!!!!!!!!!")
        print(f"you entered {user_input} and computer's choice is {computers_choice}") 
        last_step()

i = 0
while i<4:
    user_input = input(f"please enter your choice: {game_symbols}").lower()
    i +=1
    game(user_input)
    if i == 4:
        last_step()
        break