import random as rd

userWin = 0
botWin = 0

def bot():
    """
    This function will return the bot's choice.
    """
    possible = ["Rock", "Paper", "Scissors"]
    return rd.choice(possible)

while True:
    user = input("Rock, Paper, or Scissors? ")
    ans = user.lower()
    print("You choose:", ans)
    bot_ans = bot().lower()
    print("The bot chose:", bot_ans)
    
    if ans == bot_ans:
        print("It's a tie!")

    elif ans == "rock":
        if bot_ans == "paper":
            print("The bot wins!")
            botWin += 1
        else:
            print("You win!")
            userWin += 1
    elif ans == "paper":
        if bot_ans == "scissors":
            print("The bot wins!")
            botWin += 1
        else:
            print("You win!")
            userWin += 1
    elif ans == "scissors":
        if bot_ans == "rock":
            print("The bot wins!")
            botWin += 1
        else:
            print("You win!")
            userWin += 1
    else:
        print("Please enter a valid choice.")
    
    answer = input("Would you like to play again (y/n)? ")
    if answer.lower() == "n":
        break
    else:
        continue

if userWin > botWin:
    print("You win the game with " + str(userWin) + " Points!")
elif userWin < botWin:
    print("The bot wins the game with " + str(botWin) + " Points!")
else:
    print("It's a tie! You both have " + str(userWin) + " Points!")