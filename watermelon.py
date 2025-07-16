import sys

# usaco problems before dec 2020 require io from files 
# this will redirect stdio to files
# sys.stdin = open(f_name, "r")
# sys.stdout = open(f_name, "w")

readline = sys.stdin.readline
write = sys.stdout.write

w = int(readline())
if w == 2:
    write("NO\n")
else:
    write("NO\n" if w & 1 else "YES\n")