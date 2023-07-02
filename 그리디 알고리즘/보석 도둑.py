# 보석 도둑, 1202번, 백준

# my thoughts :
# 1. 가방에는 최대 한 개의 보석만이 들어갈 수 있다.따라서 최대 무게가 큰 가방에 무게가 작은 보석이 들어간다면 비효율적일 것이다.
# 2. 따라서 우리는 정렬을 이용해야 한다.
# 3. 일단 N개의 보석을 (무게, 가격)순으로 오름차순 정렬한다.
# 4. 그런다음 최대 무게가 낮은 가방부터 처리하기 위해 K개의 가방을 최대 무게 순으로 오름차순 정렬한다.
# 5. 각 가방을 처리할 때마다 최대 힙을 이용(활용)하여 각 가방에 들어갈 수 있는 보석들 중 최대가치를 골라낸다.
# 6. 이 과정을 반복해줍니다..!!
# 7. 중요한 문제이므로 나중에 다시 풀면 좋을 것 같습니다..!!

import sys
from collections import deque
import heapq

n, k = map(int, sys.stdin.readline().rstrip().split())

bosuks = list()
for _ in range(n):
    m, v = map(int, sys.stdin.readline().rstrip().split())

    bosuks.append((m, v))
bosuks.sort()
bosuks = deque(bosuks)

bags = list()
for _ in range(k):
    bags.append(int(sys.stdin.readline().rstrip()))
bags.sort()

h = [] # <<-- "각 가방에 들어갈 수 있는 보석의 가치들의 모음..!!(최대 힙으로 운용..!!)"

answer = 0

for bag in bags:
    while bosuks and bosuks[0][0] <= bag:
        heapq.heappush(h, -(bosuks.popleft())[1])
    
    if h:
        answer += -heapq.heappop(h)

print(answer)
