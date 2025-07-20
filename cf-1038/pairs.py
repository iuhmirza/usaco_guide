t = int(input())

def dist(p, q):
    return abs(p[0]-q[0]) + abs(p[1]-q[1])
    
for _ in range(t):
    n = int(input())
    points = []
    for _ in range(n):
        points.append([int(x) for x in input().split()])
    distances = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            distances[i][j] = dist(points[i], points[j])
            distances[j][i] = distances[i][j]
    count = 0    
    print(distances)
    