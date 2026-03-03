from string import printable as p

ans = set()
for x in range(18):
    for y in range(max(8, x) + 1, 18):
        num1 = int(f'5{p[x]}{p[y]}A', 18)
        num2 = int(f'18{p[x]}7', y)
        ans |= {num1 + num2}

print(len(ans))