t = int(input())
for i in range(t):
    hikes = 0
    _, k = [int(x) for x in input().split()]
    rains = [int(x) for x in input().split()]
    hikes = 0
    count = 0
    for rain in rains:
        if count == k:
            hikes += 1
            count = 0
        elif rain == 1:
           count = 0
        else:
            count += 1
    print(hikes + (1 if count == k else 0))
