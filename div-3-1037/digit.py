n = int(input())
cases = []
for i in range(n):
    cases.append(input())
for case in cases:
    print(min(int(c) for c in list(case)))