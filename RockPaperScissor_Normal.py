print('''
Rock paper scissors is a hand game originating from China, usually played between two people, in which each player simultaneously forms one of three shapes with an outstretched hand. These shapes are "rock", "paper", and "scissors".
''')

'''
Here, we will try to code the game in python and play it in the terminal.
'''

# Rules of the Game
# Rock beats Scissor, Scissor beats Paper and Paper beats Rock


# Importing random module for the computer to randomly choose between R, P and S
import random as r
from threading import Thread
from playsound import playsound
from prettytable import PrettyTable


def start():
    playsound('/Users/priyanshuranjan/Desktop/Programming/Projects/Sounds/WinBanjo.mp3')


threadStart = Thread(target=start)
threadStart.start()

# Creating a dictionary for further help in case of shortcuts in the game
dict = {
    "r": "Rock ",  # r means Rock
    "p": "Paper",  # p means Paper
    "s": "Scissor"  # s means Scissor
}


# Deciding who won the game
def gameWin(comp, you):
    # Case of both choosing the same shape
    if comp == you:
        return None

    # Case of Computer choosing Rock
    elif comp == dict["r"]:
        if you == dict["p"]:
            return True
        else:
            return False

    # Case of Computer choosing Paper
    elif comp == dict["p"]:
        if you == dict["s"]:
            return True
        else:
            return False

    # Case of Computer choosing Scissor
    else:
        if you == dict["r"]:
            return True
        else:
            return False


def game_start():
    playsound('/Users/priyanshuranjan/Desktop/Programming/Projects/Sounds/GameStart.mp3')


def good_bye():
    playsound("/Users/priyanshuranjan/Desktop/Programming/Projects/Sounds/GoodBye.mp3")


def play_winning():
    playsound('/Users/priyanshuranjan/Desktop/Programming/Projects/Sounds/Good.mp3')


def play_tie():
    playsound("/Users/priyanshuranjan/Desktop/Programming/Projects/Sounds/Tie.mp3")


def play_lose():
    playsound("/Users/priyanshuranjan/Desktop/Programming/Projects/Sounds/OhNo.mp3")


def play_scorecard():
    playsound("/Users/priyanshuranjan/Desktop/Programming/Projects/Sounds/WinFantasia.mp3")


# Welcoming the User
print("\nWelcome to Rock Paper Scissor(RPS) Game!!           Game Developed by Priyanshu Ranjan\n")

# Taking name from the User
username = input("Enter your name : ")

# For Scores of the user and computer
compScore = 0
youScore = 0

# Making an endless so that user can play his/her heart out!!
while True:

    threadGame = Thread(target=game_start)
    threadGame.start()
    # Making the computer moves
    print("\nComputer's Move... ", end='')

    # Using the randint function for generating random numbers between 1 and 3
    rand_number = r.randint(1, 3)
    if rand_number == 1:  # Taking 1 as Rock
        comp = dict["r"]
    elif rand_number == 2:  # Taking 2 as Paper
        comp = dict["p"]
    else:  # Taking 3 as Scissor
        comp = dict["s"]
    print("Computer made its move 🙂")

    # Using the while loop to ensure that the user enters correctly
    while True:
        print(username + " Move!! ", end='')
        print("Rock(r), Paper(p) or Scissor(s) ?", end=" ")
        you = input("Your Choice : ")  # Taking input from the user

        # Assigning the desired value of r, p and s
        if you == 'r':
            you = dict["r"]
            break
        elif you == 'p':
            you = dict["p"]
            break
        elif you == 's':
            you = dict["s"]
            break
        else:
            pass

    # Printing the computer's and user's choices
    print("Computer's choice is :", comp)
    print("And your choice is :", you)
    print()

    # Using gameWin function to decide who won the game
    result = gameWin(comp, you)

    # Printing the Result of the game
    if result is None:
        threadTie = Thread(target=play_tie)
        threadTie.start()
        print("The game was a TIE! 😐😐")
        compScore = compScore + 1
        youScore = youScore + 1
    elif result is True:
        threadWin = Thread(target=play_winning)
        threadWin.start()
        print(username + " WINS!!! 🤩🥳🤩")
        youScore = youScore + 2
    else:
        threadLose = Thread(target=play_lose)
        threadLose.start()
        print(username + " LOSES!! 😫😭😫")
        compScore = compScore + 2

    # Printing the scorecard
    print("\nDo you want to see the score card ?")
    print("Enter 'y' for yes and 'n' for no... ", end='')
    sc = input("Your choice : ")
    threadCard = Thread(target=play_scorecard)
    threadCard.start()
    if sc == 'y':
        myTable = PrettyTable([username, "Computer"])
        myTable.add_row([youScore, compScore])
        print(myTable)
        print()

    # Asking the user if they want to play the game again
    print("\n\nDo you want to play RPS again ?")
    print("Press 'y' to continue and 'n' to exit..", end=' ')
    ch = input("Enter your choice : ")
    if ch == 'y':
        continue
    else:
        break

# Thanksgiving to the user
threadBye = Thread(target=good_bye)
threadBye.start()
print("\nThe final score card is : ")
print(myTable)
print("\n\nThanks for playing the game " + username + "... Enjoy your day!!\n\n")

# The coding ends here....

'''
To make the whole game we can have variations of two players like having a tournaments of 10 to 15 to 20 games
Or two player can play rock paper scissor spock lizard game
We can also have a multiplayer(6) game with a tournament of 20 games
'''
