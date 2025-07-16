k, n, w = (int(x) for x in input().split())
cost_bananas = sum(k*i for i in range(1,w+1))
if cost_bananas < n:
    print(0)
else:
    print(cost_bananas-n)