from math import dist

def edge(cluster):
    res = []
    for dot in cluster:
        sum_dist=sum(dist(dot,d)for d in cluster)
        res.append([sum_dist,dot])
    return max(res)[1]

with open(r".\files\27.17.A_19566.txt") as file:
    dots = [list(map(float, i.replace(",", ".").split())) for i in file]
eps =1
clusters =[]
while dots:
    cluster = [dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if dist(dot,d)<eps:
                cluster.append(d)
                dots.remove(d)
    if len(cluster)>4:
        clusters.append(cluster)

print(len(cluster)for cluster in clusters)
edges = [edge(cluster) for cluster in clusters]

print(sum(e[0] for e in edges)/len(edges)*10000)
print(sum(e[1] for e in edges)/len(edges)*10000)