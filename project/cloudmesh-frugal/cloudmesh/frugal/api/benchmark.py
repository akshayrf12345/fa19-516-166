#!/usr/bin/env python3
import random
import string
from time import time

n=10000000
loops = 20
count=0
notcount = 0

print()
print('Running Benchmark...')

t = time()
for outer in range(loops):
    random.seed(0)
    n_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))
    for char in n_string:
        if (char == 'f'):
            count += 1
        else:
            notcount += 1
delta = time() - t
print('Created and processed a random %d length string %d times in %0.4f s.' % (n, loops,delta))