import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    # TO DO
    for _ in range(CURRENTRABBITPOP):
        if (CURRENTRABBITPOP < MAXRABBITPOP and CURRENTRABBITPOP >= 10):
            pborn = 1.0 - CURRENTRABBITPOP / float(MAXRABBITPOP)
            flip = random.random()
            
            if (flip <= pborn):
                CURRENTRABBITPOP = CURRENTRABBITPOP + 1
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    # TO DO
    for _ in range(CURRENTFOXPOP):
        peat = CURRENTRABBITPOP / float(MAXRABBITPOP)
        flip1 = random.random()
        if (flip1 <= peat and CURRENTRABBITPOP > 10):
            CURRENTRABBITPOP = CURRENTRABBITPOP - 1
            flip2 = random.random()
            if (flip2 <= 1.0/3.0):
                CURRENTFOXPOP = CURRENTFOXPOP + 1
        elif (CURRENTFOXPOP > 10):
            flip2 = random.random()
            if (flip2 <= .90):
                CURRENTFOXPOP = CURRENTFOXPOP - 1
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    # TO DO
    if (CURRENTRABBITPOP < 10 or CURRENTFOXPOP < 10):
        return ([],[])
        
    rabbits = []
    foxes = []
    
    for _ in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbits.append(CURRENTRABBITPOP)
        foxes.append(CURRENTFOXPOP)
        
    return (rabbits, foxes)

def test1():
    n = 200
    r,f = runSimulation(n)
    coeff_r = pylab.polyfit(range(len(r)), r, 2)
    coeff_f = pylab.polyfit(range(len(f)), f, 2)
        
    pylab.plot(range(n), r, label="Rabbit Count")
    pylab.plot(range(n), f, label="Fox Count")
    pylab.plot(pylab.polyval(coeff_r, range(len(r))), label="Rabbit Fit")
    pylab.plot(pylab.polyval(coeff_f, range(len(f))), label="Fox Fit")
    pylab.title('Number of critters at time t')
    pylab.xlabel('Time')
    pylab.ylabel('Count')
    pylab.legend(title="Legend")
    
 
    pylab.show()
    
    