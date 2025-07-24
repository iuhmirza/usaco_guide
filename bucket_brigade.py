import sys
# this will redirect stdio to files
sys.stdin = open("buckets.in", "r")
sys.stdout = open("buckets.out", "w")

m = {}
for i in range(10):
    row = input()
    for j, r in enumerate(row):
        if r != ".":
            m[r] = (i, j)
if m["B"][0] == m["L"][0]:
    if m["R"][0] == m["B"][0] and min(m["L"][1], m["B"][1]) < m["R"][1] < max(m["L"][1], m["B"][1]):
        print(abs(m["B"][1] - m["L"][1]) + 1)
    else:
        print(abs(m["B"][1] - m["L"][1]) - 1)
elif m["B"][1] == m["L"][1]:
    if m["R"][1] == m["B"][1] and min(m["L"][0], m["B"][0]) < m["R"][0] < max(m["L"][0], m["B"][0]):
        print(abs(m["B"][0] - m["L"][0]) + 1)
    else:
        print(abs(m["B"][0] - m["L"][0]) - 1)
else:
    print(abs(m["B"][1] - m["L"][1]) + abs(m["B"][0] - m["L"][0]) - 1)
