# number = input("pick a number: ") 
# print("this is your number,") 
# print(number) 


affirmitive_responses = ["yes","Yes","y","Y","Okay","okay","Fine","fine"]
decision = input("Hi Angus, my name is Karen. Would you like to pick a number for me? Type yes or no \n")

if decision in affirmitive_responses:
    print("pick a number") 
   
    newnumber = input()
    # print(int(newnumber)) 
    try:
        newnumber = int(newnumber) 
    except: 
        print("You didn't put in a number faggot") 
    print(newnumber , "is a very nice number well done!") 
    print("Now can I add my number to yours?")
    decision = input() 
    if decision in affirmitive_responses:
        print("666") 
else: # this will run if they dont say literally yes
    pass