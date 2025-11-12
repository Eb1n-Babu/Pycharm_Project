from itertools import groupby

input_str = "aaabbcca"

for i, group in groupby(input_str):
    print(f"{len("".join(group))}{i}",end="")
