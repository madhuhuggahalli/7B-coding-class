from pylab import *
import random

n = 2000    # number of coin tosses in each trial
t = 3000    # number of trials
trials = [sum([random.randint(0,1) for i in range(n)]) for j in range(t)]
freq = [trials.count(k) for k in range(n+1)]
bar(range(n+1), freq, align='center')
show()
