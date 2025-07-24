    
t = int(input())
for _ in range(t):
    a, b, k = [int(x) for x in input().split()]
    if a == b:
        print(1)
        continue
    if a <= k and b <= k:
        print(1)
        continue
    found = False
    for i in range(2, k+1):
        for j in range(2, k+1):
            found = found or (a % i == 0 and b % j == 0)
    if found:
        print(1)
    else:
        print(2)