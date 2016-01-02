import math, random, pylab

def takeStepEDrunk():
    ang = 2 * math.pi * random.random()
    length = 0.5 + 0.5 * random.random()
    return (length * math.sin(ang), length * math.cos(ang))
    
def takeStepPhotoDrunk():
    stepChoices = [(0.0, 0.5),(0.0, -0.5),(1.5, 0.0),(-1.5, 0.0)]
    return random.choice(stepChoices)

def takeStepColdDrunk():
    stepChoices = [(0.0,0.9), (0.0,-1.03), (1.03, 0.0), (-1.03, 0.0)]
    return random.choice(stepChoices)

def takeStepUsualDrunk():
    stepChoices = [(0.0,1.0), (0.0,-1.0), (1.0, 0.0), (-1.0, 0.0)]
    return random.choice(stepChoices)

def takeStepDDrunk():
    stepChoices = [(0.85, 0.85), (-0.85, -0.85), (-0.56, 0.56), (0.56, -0.56)] 
    return random.choice(stepChoices)
    
xVals = []
yVals = []
for i in range(1000):
    steps = [takeStepUsualDrunk() for _ in range(1000)]
    x = sum([x for (x,_) in steps])
    y = sum([y for (_,y) in steps])
    xVals.append(x)
    yVals.append(y)
    
pylab.plot(xVals,yVals,"o")
pylab.ylim([-100,100])
pylab.xlim([-100,100])
pylab.show()