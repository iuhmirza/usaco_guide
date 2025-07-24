t = int(input())

for _ in range(t):
    contest = list(input())
    count = [0] * 26
    for ch in contest:
        count[ord(ch)-ord("A")] += 1
    new_contest = "T"*count[ord("T")-ord("A")]
    
    for i, c in enumerate(count):
        if chr(i+ord("A")) == "T":
            continue
        new_contest += chr(i+ord("A")) * c

    print(new_contest)