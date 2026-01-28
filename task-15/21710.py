from itertools import combinations


def f(x):
    B = 36 <= x <= 75
    C = 60 <= x <= 110
    A = A1 <= x <= A2

    return (not A) <= (B == C)


line_A = [36, 75, 60, 110]
line_X = [40, 70, 80]
ans = []
for A1, A2 in combinations(line_A, 2):
    if all(f(x) for x in line_X):
        ans.append(A2 - A1)
print(min(ans))
