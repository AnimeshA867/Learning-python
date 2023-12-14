import random
import math
import os
num= math.ceil(random.randrange(1,100000))

gameFinished=False;

while not gameFinished:
        x= int(input("Guess the number:"))  
        if(x==num):
            print("Yay. You got it.")
        else:
            if x > num:
                   print("Guess lower.")
            elif x<num:
                  print("Guess higher.")
      
