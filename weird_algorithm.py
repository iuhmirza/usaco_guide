import sys

readline = sys.stdin.readline
write = sys.stdout.write

n = int(readline())
o = ""
while n != 1:
    o += str(n)
    o += " "
    if n & 1:
        n = n*3 + 1
    else:
        n = n // 2
o += "1"
print(o)