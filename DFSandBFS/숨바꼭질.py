# 숨바꼭질, 1697번, 백준

# my thoughts :
# 1. By using BFS, We can solve it..!!

import sys
from collections import deque

n, k = map(int, sys.stdin.readline().rstrip().split())

# 만약 초기 상태에서 수빈이의 위치가 동생의 위치보다 크다면 무조건 걷기를 이용하여 동생의 위치까지 가야합니다.
if n >= k:
    print(n - k)
    exit()
else:
    pass

visited = [False] * (100_001)
queue = deque()

visited[n] = True
queue.append((0, n))

while queue:
    cur_cnt, cur_v = queue.popleft()

    if cur_v == k:
        print(cur_cnt)
        break # <==> exit()

    # 걷기
    for new_v in [cur_v - 1, cur_v + 1]:
        if 0 <= new_v <= 100_000 and not visited[new_v]:
            visited[new_v] = True
            queue.append((cur_cnt + 1, new_v))
    
    # 순간이동
    for new_v in [cur_v * 2]:
        if 0 <= new_v <= 100_000 and not visited[new_v]:
            visited[new_v] = True
            queue.append((cur_cnt + 1, new_v))
