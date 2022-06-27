print("Welcome to my first Python quiz game")

# ask users if they want to play the game/ if not the game will be quit
# as a java native , input() is like scanner system in

playing =input("Do you want to play?(enter yes/no) ")

if playing !="yes":
    quit()

print("Greate! let's start the quiz :)")

answer = input("What does CPU stands for? ")
if answer == "central proccessing unit":
    print("Correct! :)")
else:
    print("Incorrect! :(")