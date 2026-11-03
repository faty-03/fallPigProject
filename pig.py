import random

def roll():
    return random.randint(1,6)
def pigTurn():
    turnTotal = 0  
    rollOne = False  
    while turnTotal < 20 and not rollOne:
        dice = roll()
        if dice == 1:
            turnTotal = 0
            rollOne = True
        else:
            turnTotal += dice
    print("Turn total:", turnTotal)
        
print(pigTurn())
