# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in xrange(2**N):
        combo = []
        for j in xrange(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo
        
def yieldAllCombos(items):
    sets = [s for s in powerSet(items)]
    for s in sets:
        for s2 in sets:
            if not any(z in s for z in s2):
                yield (s,s2) 

myItems = ['a','b']
#myItems = [i for i in range(10)]
print [b for b in yieldAllCombos(myItems)]