##########################################
#  d = (t-s)*s = ts - s^2   for d=distance, t=time, s=speed
#  s such that 0 < -s^2 + ts - d is when we win
#  we will calculate this using the quadratic formula
##########################################
from math import sqrt, floor, ceil

def quadraticFormula(a, b, c):
    # given the problem, we don't need to handle the case where 
    # the input to sqrt() is negative
    pos = -b + sqrt(b**2 - (4*a*c))
    neg = -b - sqrt(b**2 - (4*a*c))

    return pos/(2*a), neg/(2*a)


times, dists= [string.split() for string in open('../input/input_6.txt', 'r').read().split('\n')]

error_margin = 1

for i in range(1, len(dists)):
    d = int(dists[i])
    t = int(times[i])

    x, y = quadraticFormula(-1, t, -d)

    if x >= y:
        wins = ceil(x) - floor(y) - 1
    else:
        wins = ceil(y) - floor(x) - 1

    error_margin*=wins

print(error_margin)