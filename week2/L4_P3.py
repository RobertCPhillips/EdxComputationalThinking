# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 19:52:47 2015

@author: robertc
"""

import math

def stdDevOfLengths(L):
    if len(L) == 0:
        return float('NaN')
        
    lengths = [float(len(l)) for l in L]
    count = float(len(lengths))
    
    mean = sum(lengths) / float(count)
    sd = math.sqrt(1/count * sum([(l-mean)**2 for l in lengths]))
    
    return sd