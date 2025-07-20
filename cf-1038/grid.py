t = int(input())
for _ in range(t):
    n, m = [int(x) for x in input().split()]
    if n >= 2 and m >= 3:
        print("YES")
    elif n >= 3 and m >= 2:
        print("YES")
    else:
        print("NO")