import pylab, random

class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)
        
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a list of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axes
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.hist(values, numBins)
    if not title is None:
        pylab.title(title)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    pylab.show()

def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    runs = []
    for i in range(numTrials):
        rolls = [die.roll() for _ in range(numRolls)]
        #print(rolls)
        run = 1
        largestRun = 1
        face = None
        for r in rolls:
            if r == face:
                run = run + 1
            else:
                if run > largestRun:
                    largestRun = run 
                run = 1
                face = r
        if run > largestRun:
            largestRun = run
        runs.append(largestRun)
        
    makeHistogram(runs, 10,'Size of Run', 'Frequency of a Run')  
    #print(runs)  
    return sum(runs)/float(numTrials)