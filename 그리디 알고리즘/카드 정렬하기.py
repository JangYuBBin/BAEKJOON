# 카드 정렬하기, 1715번, 백준

# my thoughts :
# 1. By using Min Heap, We can solve it..!!

import sys
import heapq

n = int(sys.stdin.readline().rstrip())

h = []

for _ in range(n):
    heapq.heappush(h, int(sys.stdin.readline().rstrip()))

answer = 0

while len(h) >= 2:
    num1 = heapq.heappop(h)
    num2 = heapq.heappop(h)

    answer += num1 + num2

    heapq.heappush(h, num1 + num2)

print(answer)
