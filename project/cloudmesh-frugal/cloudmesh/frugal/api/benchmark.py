#!/usr/bin/env python3
import random
import string
from time import time


random.seed(0)

n=10000000

print()
print('Running Benchmark...')

t = time()
n_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))
delta = time() - t
print('Created a random %d length string in %0.4f s.' % (n, delta))

t = time()
count=0
notcount = 0
for char in n_string:
    if (char == 'f'):
        count += 1
    else:
        notcount += 1
delta = time() - t
print('Processed a random %d length string in %0.4f s.' % (n, delta))