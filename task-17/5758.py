from itertools import combinations
with open (r".\files\17_5758.txt") as file:
    data =[int(i) for i  in file]
for x,y in combinations(data,2):
    # https: // kompege.ru / variant?kim = 25172546