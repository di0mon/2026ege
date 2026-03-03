def f(x, s):
    if x <= 11: return s % 2 == 0
    if s == 0: return False
    h = [f(x - 3, s - 1), f(x - 3, s - 1), f(x // 3, s - 1)]
    return any(h) if (s - 1) % 2 == 0 else all(h)


print("19", [x for x in range(12, 1000) if f(x, 2)])
print("19", [x for x in range(12, 1000) if not f(x, 1) and f(x, 3)])
print("19", [x for x in range(12, 1000) if not f(x, 2) and f(x, 4)])
