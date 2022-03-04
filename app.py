import random
number=random.randint(1,99)
guess=int(input("Guess the Number ::- "))
while number != "string":
    diff=number-guess
    if guess != number:
        hint=input("Wrong Answer !! If you want a hint press 'y', if not needed press 'n' ::- ")
        if hint=="y":
            print("The number is {} steps away from you".format(diff))
        else:
            print("Alright!! Try Again")
        guess=int(input("Guess Again ::- "))
    else:
        print("YaHHH !!! You guessed it !!")
        break