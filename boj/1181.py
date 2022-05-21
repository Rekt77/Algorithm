import sys

N = int(sys.stdin.readline())
words = list(set([sys.stdin.readline().strip() for _ in range(N)]))
words.sort(key=lambda x: (len(x), x))
for each in words:
    print(each)