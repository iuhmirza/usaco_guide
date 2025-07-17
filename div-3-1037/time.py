t = int(input())
for _ in range(t):
    num_casinos, k = [int(x) for x in input().split()]
    casinos = []
    for _ in range(num_casinos):
        casinos.append([int(x) for x in input().split()])
    casinos.sort()
    for min_amount, max_amount, real in casinos:
        if real > k and min_amount <= k <= max_amount:
            k = real
    print(k)
    # looks like an intervals question
