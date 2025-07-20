t = int(input())
for _ in range(t):
    n = int(input())
    piles = []
    ops = 0
    for _ in range(n):
        piles_current.append([int(x) for x in input().split()])
    def dfs():
    print(piles_current)
    # moving a zero costs 1
    # moving a one costs 2 if zeros else 1
    print("----")
