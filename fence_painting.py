import sys

# usaco problems before dec 2020 require io from files 
# this will redirect stdio to files
sys.stdin = open("paint.in", "r")
sys.stdout = open("paint.out", "w")

readline = sys.stdin.readline
write = sys.stdout.write

a, b = (int(x) for x in readline().split())
c, d = (int(x) for x in readline().split())
count = 0
if (b < c) or (d < a):
    count = b-a + d-c
else:
    count = max(int(b),int(d)) - min(int(a),int(c))
write(str(count)+"\n")