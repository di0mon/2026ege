with open(r'.\files\17_3749.txt') as file:
    data = [int(i) for i in file]

max_sqrt = max(i for i in data if i ** .5 % 1 == 0)

ans = []
for num1, num2 in zip(data, data[1:]):
    if (num1 * num2) ** .5 % 1 == 0:
        u1 = num1 <= max_sqrt * 3
        u2 = num2 <= max_sqrt * 3
        if u1 + u2 >= 1:
            ans.append((num1 * num2) ** .5)

print(len(ans), max(ans) + min(ans))