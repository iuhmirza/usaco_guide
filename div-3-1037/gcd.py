t = int(input())
for _ in range(t):
    _ = input()
    pxyz = [int(x) for x in input().split()]
    i = 1
    while i < len(pxyz):
        if pxyz[i-1] % pxyz[i] != 0:
            break
        i += 1
    if i != len(pxyz):
        print("NO")
        continue
    sxyz = [int(x) for x in input().split()]
    i = 1
    while i < len(sxyz):
        if sxyz[i] % sxyz[i-1] != 0:
            break
        i += 1
    if i != len(sxyz):
        print("NO")
        continue
    for p, q in zip(pxyz, sxyz):
        p, q = max(p, q), min(p, q)
        if p % q != 0:
            break
    if p % q != 0:
        print("NO")
    else:
        print("YES")