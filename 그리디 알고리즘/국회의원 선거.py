# 국회의원 선거, 1417번, 백준

# my thoughts :
# 1. By using Heap, We can solve it..!!

import sys
import heapq

n = int(sys.stdin.readline().rstrip())

dasom = int(sys.stdin.readline().rstrip())

h = []

for _ in range(n - 1):
    heapq.heappush(h, -int(sys.stdin.readline().rstrip()))

answer = 0

if n == 1:
    print(answer)
    exit()

while -h[0] >= dasom:
    answer += 1

    val = heapq.heappop(h)
    val += 1
    heapq.heappush(h, val)
    
    dasom += 1

print(answer)
