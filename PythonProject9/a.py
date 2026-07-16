from itertools import groupby

from numpy.f2py.auxfuncs import flatlist

x = "uwwwfhhhff"

for i, group in groupby(x):
    print(f"{i}{len("".join(group))}",end="")

a = [[1,2,3],[3,4],[4,5,6],[7,8,9],[4,5]]
print(flatlist(a))



