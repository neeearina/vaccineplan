from itertools import *


k = 0
for x in permutations("АСИН", r=7):
    k += 1
print(k)
