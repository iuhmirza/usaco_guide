import sys

# usaco problems before dec 2020 require io from files 
# this will redirect stdio to files
sys.stdin = open("promote.in", "r")
sys.stdout = open("promote.out", "w")

readline = sys.stdin.readline
write = sys.stdout.write

p = []
for i in range(4):
    p.append([int(x) for x in readline().split()])


q = [0] * 4
diff = 0
for i in range(3, -1, -1):
    diff += p[i][1] - p[i][0]
    if diff > 0:
        q[i] = diff
    
for x in q[1:]:
    print(x)

# for i in range(4):
#     diff = p[i][1] - p[i][0]
        