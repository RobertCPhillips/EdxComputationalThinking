import random

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    bucket = ['R','G','R','G','R','G','R','G']
    draws = [random.sample(bucket, 3) for _ in range(numTrials)]
    count = sum([x == ['R','R','R'] or x == ['G','G','G'] for x in draws])
    
    return float(count)/float(numTrials)