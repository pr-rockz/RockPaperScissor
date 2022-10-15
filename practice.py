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

def wholeGame():
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
    return result



print()
print("Want to play it endlessly? Press 1")
print("Want to play a 10 Game Tournament? Press 2")
print("Want to play a 20 Game Tournament? Press 3")

numberOfGames = int(input("Enter your choice : "))
print()


if numberOfGames == 1:
    while True:
        resultGame = wholeGame()
        # Printing the Result of the game
        if resultGame is None:
            threadTie = Thread(target=play_tie)
            threadTie.start()
            print("The game was a TIE! 😐😐")
            compScore = compScore + 1
            youScore = youScore + 1
        elif resultGame is True:
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

elif numberOfGames == 2:
    for i in range(10):
        print(f"\nYour {i+1}th game :")
        resultGame = wholeGame()
        if resultGame is None:
            threadTie = Thread(target=play_tie)
            threadTie.start()
            print("The game was a TIE! 😐😐")
            compScore = compScore + 1
            youScore = youScore + 1
        elif resultGame is True:
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

elif numberOfGames == 3:
    for i in range(20):
        print(f"\nYour {i+1}th game :")
        resultGame = wholeGame()
        if resultGame is None:
            threadTie = Thread(target=play_tie)
            threadTie.start()
            print("The game was a TIE! 😐😐")
            compScore = compScore + 1
            youScore = youScore + 1
        elif resultGame is True:
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

else:
    print("Wrong number entered.")



# Thanksgiving to the user
threadBye = Thread(target=good_bye)
threadBye.start()
print("\n\n\nThe final score card is : ")
finalTable  = PrettyTable([username], "Computer")
finalTable.add_row([youScore, compScore])
print(finalTable)
print("\n\nThanks for playing the game " + username + "... Enjoy your day!!\n\n")

# The coding ends here....