from itertools import combinations
def f(x):
    P = 10 <= x <= 150
    Q = 160 <= x <= 250
    R = 240 <= x <= 300
    A = A1 <= x <= A2
    return Q<=P or (not A) <=R
line_A=[1,83,94,100]
line_X=[50,88,95]
ans=[]
for A1,A2 in combinations(line_A,2):
    if all(f(x) for x in line_X):
        ans.append(A2-A1)
print(max(ans))