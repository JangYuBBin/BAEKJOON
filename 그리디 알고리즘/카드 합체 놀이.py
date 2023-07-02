# 카드 합체 놀이, 15903번, 백준

import sys
import heapq

n, m = map(int, sys.stdin.readline().rstrip().split())

arr = list(map(int, sys.stdin.readline().rstrip().split()))

h = []

for val in arr:
    heapq.heappush(h, val)

for _ in range(m):
    val1 = heapq.heappop(h)
    val2 = heapq.heappop(h)

    heapq.heappush(h, val1 + val2)
    heapq.heappush(h, val1 + val2)

print(sum(h))
