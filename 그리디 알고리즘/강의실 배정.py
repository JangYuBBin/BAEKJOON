# 강의실 배정, 11000번, 백준

# my thoughts :
# 1. 일단 N개의 수업을 (시작시각, 끝나는 시각) 기준으로 오름차순 정렬한다.
# 2. 강의실 현황을 최소 힙으로 나타낸다.
# 3. ....
# 4. 중요한 문제이므로 나중에 다시 풀어보면 좋을 것 같습니다..!!

import sys
import heapq

n = int(sys.stdin.readline().rstrip())

arr = list()

for _ in range(n):
    s, t = map(int, sys.stdin.readline().rstrip().split())

    arr.append((s, t))

arr.sort()

h = []

for start, end in arr:
    if not h:
        heapq.heappush(h, end)
    else:
        if h[0] <= start:
            heapq.heappop(h)
            heapq.heappush(h, end)
        else:
            heapq.heappush(h, end)

print(len(h))
