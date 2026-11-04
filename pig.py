import random
def roll():
    return random.randint(1,6)
def pigTurn(target = 20):
    turnTotal = 0  
    rolledOne = False  
    while turnTotal < target and not rolledOne:
        dice = roll()
        #print("Roll:", dice)
        if dice == 1:
             turnTotal = 0
             rolledOne = True
        else:
             turnTotal += dice
    #print("Turn total:", turnTotal)
    return turnTotal
def holdAtXSims(trials,target = 20):
    results = {0:0}
    for i in range(6):
        results[target + i] = 0
    #results[target] = 0
    #results[target + 1] = 0
    #results[target + 2] = 0
    #results[target + 3] = 0
    #results[target + 4] = 0
    #results[target + 5] = 0'''
    for _ in range(trials):
        turnTotal = pigTurn(target)
        results[turnTotal] += 1
    print("Turn total\t\tEstimated Prob")
    for turnTotal in results:
        print(turnTotal,results[turnTotal]/trials,sep="\t\t")
print(holdAtXSims(100000,25))
