import pylab
import random

doors = [1,2,3,4]

def montyChoose(guessDoor, prizeDoors):
    goats = [x for x in doors if x not in prizeDoors]
    return random.choice(goats)

def randomChoose(guessDoor, prizeDoor):
    notGuess = [x for x in doors if x != guessDoor]
    return random.choice(notGuess)
    
def simMontyHall(numTrials, chooseFcn):
    stickWins, switchWins, noWin = (0, 0, 0)
    for t in range(numTrials):
        guess = random.choice(doors)
        prizeDoors = random.sample(doors,2)
        toOpen = chooseFcn(guess, prizeDoors)
        if toOpen in prizeDoors:
            noWin += 1
        elif guess in prizeDoors:
            stickWins += 1
            
        switchTo = random.choice([x for x in doors if x not in [guess, toOpen]])
        if switchTo in prizeDoors:
            switchWins += 1

    return (stickWins, switchWins)

def displayMHSim(simResults, title):
    stickWins, switchWins = simResults
    pylab.pie([stickWins, switchWins],
              colors = ['r', 'c'],
              labels = ['stick', 'change'],
              autopct = '%.2f%%')
    pylab.title(title)

simResults = simMontyHall(100000, montyChoose)
print simResults
displayMHSim(simResults, 'Monty Chooses a Door')
pylab.figure()
simResults = simMontyHall(100000, randomChoose)
displayMHSim(simResults, 'Door Chosen at Random')
pylab.show()
