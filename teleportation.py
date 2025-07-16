import sys

# usaco problems before dec 2020 require io from files 
# this will redirect stdio to files
sys.stdin = open("teleport.in", "r")
sys.stdout = open("teleport.out", "w")

readline = sys.stdin.readline
write = sys.stdout.write

start, end, x, y = (int(i) for i in readline().split())
x_to_y = 0
start_to_x = abs(start-x)
start_to_y = abs(start-y)
end_to_x = abs(end-x)
end_to_y = abs(end-y)
start_to_end = abs(start-end)
print(min(start_to_x+end_to_y, start_to_y+end_to_x, start_to_end))