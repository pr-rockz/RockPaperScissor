print()
print("\u001b  ✦✧✦ ⚔︎⚔︎  Rock Paper Scissor Ultimate!!  ⚔︎⚔︎ ✦✧✦")

print('''
\nRock paper scissors is a hand game originating from China, usually played between two people, in which each player simultaneously forms one of three shapes with an outstretched hand. These shapes are "rock", "paper", and "scissors".
''')

'''
Here, we will try to code the game in python and play it in the terminal.
'''

# Rules of the Game
# Rock beats Scissor, Scissor beats Paper and Paper beats Rock


from threading import Thread

from playsound import playsound


# import colorama
# from colorama import Fore


def play_game_ultimate():
    playsound('/Users/priyanshuranjan/Desktop/Programming/Projects/Sounds/SuccessFanfareTrumpets.mp3')


threadUltimate = Thread(target=play_game_ultimate)
threadUltimate.start()


print("\nPress 1 to play normal Rock Paper Scissor.")
print("Press 2 to play Rock Paper Scissor Liazrd Spock.")
print("Press 3 to play Rock Paper Scissor with 2 computers simultaneously.")
print("Press 4 to play Rock Paper Scissor Visually.")
print("Press 5 to play Rock Paper Scissor Lizard Spock Visually.")
print("Press any other number to exit.")

choice = int(input("\nEnter your choice : "))

if choice == 1:
    import practice

elif choice == 2:
    import RockPaperScissorLizardSpock

elif choice == 3:
    import RockPaperScissor_2Comp