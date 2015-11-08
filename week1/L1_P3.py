import pylab
import numpy as np

def getTemps(fileName):
  lines = [line.rstrip('\n').split()[1:] for line in open(fileName) if len(line) > 0 and line[0].isdigit()]
  low = [int(l[1]) for l in lines]
  high = [int(h[0]) for h in lines]
  
  return (low, high)
  
def producePlot(lowTemps, highTemps):
  diffTemps = list(np.array(highTemps) - np.array(lowTemps))
  pylab.plot(range(1, len(diffTemps)+1), diffTemps)
  pylab.title('Day by Day Ranges in Temperature in Boston in July 2012')
  pylab.xlabel('Days')
  pylab.ylabel('Temperature Ranges')
  pylab.show()
  
low, high = getTemps(fileName = 'julyTemps.txt')
producePlot(low, high)