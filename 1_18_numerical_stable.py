"""Softmax."""
import numpy as np

a = 1e9
times = int(1e6)
for i in xrange(times):
    a = a + 1e-6
print a - 1e9
