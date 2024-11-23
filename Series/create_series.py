"""
Create a series of 10 elements, random integers from 70 to 100, representing scores
on a monthly exam. Set the index to be the month names, starting in September and
ending in June. (If these months don’t match the school year in your location, feel
free to make them more realistic.)
"""
import numpy as np
from pandas import Series

g = np.random.default_rng(0)
s = Series(g.integers(70, 101, 10))
s.index = 'Sep Oct Nov Dec Jan Feb Mar Apr May Jun'.split()
print(s)
