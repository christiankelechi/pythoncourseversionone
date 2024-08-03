import random 

name=input("Enter your name to start playing ludo game \n")

print(f" HI , {name} , "+
"to this ludo game , you can toast the dice to get an output and also play your game\n")
ludo_ouput=random.randrange(1,7)

print(ludo_ouput)

if ludo_ouput==6:
    print("Enter a new entity")
    
else:
    print("just increment any existing entity")