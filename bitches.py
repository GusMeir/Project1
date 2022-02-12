########################## MODULES GO AT THE TOP
# if they are not imported before they are used it will crach this is because python is a script and interpreted line by line 
import pandas as pd
import numpy as np 

#### CONTANTS
affirmitive_responses = ["yes","Yes","y","Y","Okay","okay","Fine","fine"]


###################################### MAIN
if __name__ == "__main__":
    
    name = input("I am Karen, who am I speaking to?\n")

    decision = input("Hi " + name + ". Would you like to pick a number for me? Type yes or no \n")

    if decision in affirmitive_responses:
    
        newnumber = input("pick a number\n")

       # make sure the value can be turned into an integer otherwise tell them they are stupid 
       
        wrong_attempts = 0  
        while type(newnumber) is str:
            try:
                newnumber = int(newnumber) 
            except: 
                print("You didn't put in a number faggot") 
                wrong_attempts += 1 
                annoy = wrong_attempts*"new "
                newnumber = input("pick a " + annoy + "number\n")


        decision = input("Now can I add my number to yours?") 

        if decision in affirmitive_responses:
            print("666") 

    else: # this will run if they dont say literally yes
        print("Well I'd like to talk to yoour manager, you fat cunt. I'm angry, go kill yourself now please")