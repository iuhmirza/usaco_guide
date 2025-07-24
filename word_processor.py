import sys
# this will redirect stdio to files
sys.stdin = open("word.in", "r")
sys.stdout = open("word.out", "w")

N, K = [int(x) for x in input().split()]
line = []
count = 0
sentence = input().split()

for word in sentence:
    if count + len(word) <= K:
        line.append(word)
        count += len(word)
    else:
        print(" ".join(line))
        line.clear()
        line.append(word)
        count = len(word)
print(" ".join(line))