# 스네이크버드, 16435번, 백준

import sys

n, l = map(int, sys.stdin.readline().rstrip().split())

arr = list(map(int, sys.stdin.readline().rstrip().split()))

arr.sort()

for val in arr:
    if val <= l:
        l += 1
    else:
        pass

print(l)
