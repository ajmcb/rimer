from random import randint
import time
import sys

x=20
y=45


#Mrs. Brown's Boys board game timer for use when there are only two thirds of the required AAA batteries in your flat

#Generate a random number between two integer values x and y
rand = randint(x,y)
print(rand)

#Countdown timer
time.sleep(rand)
print("finished")

#Make macbook beep when finished counting down
sys.stdout.write('\a')
sys.stdout.flush()
