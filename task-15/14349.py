from itertools import combinations
def f(x):
    B = 54 <= x <= 120
    C = 78 <= x <= 151
    A = A1 <= x <= A2
    return C <= ((B and (not A))<= (not C))
line_A=[54,78,120,151]
line_X=[60,88,130]
ans=[]
for A1,A2 in combinations(line_A,2):
    if all(f(x) for x in line_X):
        ans.append(A2-A1)
print(min(ans))