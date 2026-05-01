with open(r"..\files\24_1975.txt") as file:
    data = file.readlines()

while "PP" in data:
    data = data.replace("PP", "P P")
data = data.split()


print(len(max(data, key=len)))


with open(r"..\..\files\24_1975.txt") as file:
    data = file.readlines()
cnt = 1
ans = 0
for i in range(len(data)-1):
    if data[i] + data[i+1] != "PP":
        cnt+=1
    else:
        cnt =1
    ans = max(ans,cnt)
print(ans)