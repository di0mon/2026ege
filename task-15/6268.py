from itertools import combinations
def f(x):
    B = 23 <= x <= 37
    C = 41 <= x <= 73
    A = A1 <= x <= A2
    return not(((not B)<=C)<=A)
line_A=[23,37,41,73]
line_X=[24,38,42]
ans=[]
for A1,A2 in combinations(line_A,2):
    if all(f(x) for x in line_X):
        ans.append(A2-A1)
print(min(ans))