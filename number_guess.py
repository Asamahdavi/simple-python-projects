#goal: generate random numbers and check weather how many users can guess 

#importing random module
from mimetypes import guess_extension
import random

#randrange include first input, but do not include secound input (from -10 to 10)
#randint include both (from -10 to -11)

topRange= input("Please enter the ending of the random range:")

if topRange.isdigit():
    topRange= int(topRange)

    if topRange <=0:
        print("Please type a number larger than 0 the next time")
        quit()
else:
     print("Please type a number next time")
     quit()

ran = random.randint(0,topRange)
guesses=0

while True:
    guesses+=1
    userGuess= input("Make a guess:")
    if userGuess.isdigit():
        userGuess= int(userGuess)

        
    else:
        print("Please type a number next time")
        continue
    if userGuess == ran:
        print("yeey you got it !!!")
        break
    else:
        print("you got it wrong!")

        if userGuess > ran:
            print("You were above the number !")
        else:
            print("You were below the number !")

#here with , it is smart enough to undrestand the int and string and it will convert it itself
print("You got it in",guesses,"guesses")

