from itertools import groupby

x = "uwwwfhhhff"

for i, group in groupby(x):
    x = len(''.join(group))
    print(f'{i}{x}',end="")