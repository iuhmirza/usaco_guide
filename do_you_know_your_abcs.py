import heapq
seven = [int(x) for x in input().split()]
seven.sort()
k = [seven[0], seven[1], seven[6]-seven[0]-seven[1]]
print(*k)