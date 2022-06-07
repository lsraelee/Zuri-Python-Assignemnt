import random

R = "R"
P = "P"
S = "S"
listOfOutcome = [R, P, S]
print("\n WELCOME, HOW ABOUT WE PLAY A GAME OF CHANCE - ROCK, PAPER, SCISSORS \n")


def game():
    player = input("Please Enter Your Name: ")
    if player == str():
        print("You haven't entered a name\n")
        game()
    print("\n Hello %s, let's Play" % player)
    players_input = False
    while players_input == False:
        Players_Input = str.upper(input("\n Pick an option between Rock, Paper, and Scissors\n "
                                        "(Note: R for Rock, P for Paper and S for Scissors) - "))
        Computer_Choice = random.choice(listOfOutcome)
        if Players_Input in listOfOutcome:
            players_input = True
            if Players_Input == R and Computer_Choice == P:
                print("\n Player ROCK : Computer PAPER \n")
                print("Computer WINS and %s LOSE" % player)
            if Players_Input == R and Computer_Choice == S:
                print("\n Player ROCK : Computer SCISSORS \n")
                print(" Computer LOSE and %s WON" % player)
            if Players_Input == S and Computer_Choice == R:
                print("\n Player SCISSORS : Computer ROCK \n")
                print(" Computer WINS and %s LOSE" % player)
            if Players_Input == S and Computer_Choice == P:
                print("\n Player SCISSORS : Computer PAPER \n")
                print(" Computer LOSE and %s WON" % player)
            if Players_Input == P and Computer_Choice == S:
                print("\n Player PAPER : Computer SCISSORS \n")
                print(" Computer WINS and %s LOSE" % player)
            if Players_Input == P and Computer_Choice == R:
                print("\n Player PAPER : Computer ROCK \n")
                print(" Computer LOSE and %s WON" % player)
            elif Players_Input == Computer_Choice:
                print("\n Player %s : Computer %s" % (Players_Input, Computer_Choice))
                print("It's a tie %s, TRY AGAIN \n" % player)
                game()
        else:
            players_input = False
            print("\n Error, Invalid input. Please enter the valid option  \n")


game()
