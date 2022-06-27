print("Welcome to my first Python quiz game")

# ask users if they want to play the game/ if not the game will be quit
# as a java native , input() is like scanner system in

playing =input("Do you want to play?(enter yes/no) ")

if playing.lower() !="yes":
    quit()

print("Greate! let's start the quiz :)")
#print("Please enter with lowercase")

answer = input("What does CPU stands for? ")
if answer.lower()  == "central proccessing unit":
    print("Correct! :)")
else:
    print("Incorrect! :(")

answer = input("What does WWW stands for? ")
if answer.lower()  == "world wide web":
    print("Correct! :)")
else:
    print("Incorrect! :(")

answer = input("What does HTML stands for? ")
if answer.lower()  == "hypertext markup language":
    print("Correct! :)")
else:
    print("Incorrect! :(")

answer = input("What does CSS stands for? ")
if answer.lower()  == "cascading style sheets":
    print("Correct! :)")
else:
    print("Incorrect! :(")