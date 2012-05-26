# Name : Richard McKeever
# Course : Csci 1521
# Date : November 09, 2011
# file: Program 9
# A program that simulates the out come of a craps game
from random import randrange

def rollDice():
        dice1 = randrange(1,7)
        dice2 = randrange(1,7)
        diceTotal = dice1 + dice2
        return diceTotal

def simulateGame(n):
        wins = 0
        losses = 0

        for i in range(n):
                point = 0#need to pass information to point in the loop
                firstTry = rollDice()
                
                if firstTry == 7 or firstTry == 11:
                        wins = wins + 1
                        
                elif firstTry == 2 or firstTry == 3 or firstTry == 12:
                        losses = losses + 1
                        
                else:
                        while point != firstTry and point!=7:
                                point = rollDice()
                                
                        if point == firstTry:
                                
                                wins = wins +1

                        else:
                                # point == 7:
                                
                                losses = losses+1

                
        return wins, losses
def main():
        n = eval(input("How many games would you like to simulate ? "))
        wins, losses = simulateGame(n)
        p = round(wins/(wins + losses)*100,2)
        print("The simulation produced a win percentage of %{0}".format(p))
        print("The Craps Simulation produced", wins, "wins and", losses, "losses.")
main()

