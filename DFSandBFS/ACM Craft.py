# ACM Craft, 1005번, 백준

# my thoughts :
# 1. 간선의 방향을 반대로 뒤집어서 BFS를 활용한다.
# 2. 즉, 백준이가 승리하기 위해 건설해야 할 건물의 번호인 w번호를 가지는 건물을 시작으로 탐색을 시작한다.
# 3. 각 건물까지 짓는데 걸리는 시간을 지속적으로 최댓값으로 갱신해주면서 탐색을 진행한다.
# 4. 오히려 동적 계획법 문제라기보다는 탐색 문제에 가깝다고 볼 수 있다..!!
# 5. 다음에 다시 풀어보아야할 문제인 것 같습니다..!!

import sys
from collections import defaultdict
from collections import deque

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n, k = map(int, sys.stdin.readline().rstrip().split())

    time = [0] + list(map(int, sys.stdin.readline().rstrip().split())) # <<-- "각 번호의 건물을 짓기위해 필요한 시간..!!"

    graph = defaultdict(list)

    for _ in range(k):
        v2, v1 = map(int, sys.stdin.readline().rstrip().split())

        graph[v1].append(v2)

    start_v = int(sys.stdin.readline().rstrip()) # <<-- "백준이가 승리하기 위해 건설해야 할 건물의 번호..!!"

    times = [0] * (n + 1) # <<-- "시작 건물에서 각 건물까지 걸리는 시간"
    queue = deque()

    times[start_v] = time[start_v]
    queue.append(start_v)

    while queue:
        cur_v = queue.popleft()

        for new_v in graph[cur_v]:
            if times[new_v] < times[cur_v] + time[new_v]:
                times[new_v] = times[cur_v] + time[new_v]
                queue.append(new_v)
    
    print(max(times))
