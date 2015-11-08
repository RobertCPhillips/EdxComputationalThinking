import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    bucket = ['R','G','R','G','R','G']
    draws = [random.sample(bucket, 3) for _ in range(0,numTrials)]
    count = sum([x == ['R','R','R'] or x == ['G','G','G'] for x in draws])
    
    return float(count)/float(numTrials)

print noReplacementSimulation(100)