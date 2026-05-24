#Rock paper scissor game 

import random
uscore=0
cscore=0

choice=['rock','paper','scissor']

print("Welcome to Rock-Paper-Scissors Game!")
print("Rules:")
print("Rock beats Scissor, Scissor beats Paper, Paper beats Rock")
print("You get 2 points for winning, 1 point each for a tie, 0 for losing\n")

# Loop to play multiple rounds

while(True):
     
     uch=input("Write you choice(Rock,Paper,Scissor)").lower()

     cch=random.choice(choice)

     if uch == 