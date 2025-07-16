import sys

# usaco problems before dec 2020 require io from files 
# this will redirect stdio to files
# sys.stdin = open(f_name, "r")
# sys.stdout = open(f_name, "w")

readline = sys.stdin.readline
write = sys.stdout.write

n = int(readline())
problems = 0
for i in range(n):
    problems += 1 if sum(int(x) for x in readline().split()) > 1 else 0
print(problems)