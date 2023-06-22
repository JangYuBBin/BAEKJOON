# DFS와 BFS, 1260번, 백준

# my thoughts :
# 1. By using DFS and BFS, We can solve it..!!

import sys
from collections import defaultdict
from collections import deque

n, m, v = map(int, sys.stdin.readline().rstrip().split())

graph = defaultdict(list)

for _ in range(m):
    v1, v2 = map(int, sys.stdin.readline().rstrip().split())

    graph[v1].append(v2)
    graph[v2].append(v1)

for k in graph.keys():
    graph[k].sort() # <<-- "단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, ...."

# dfs
visited = [False] * (n + 1)

def dfs(cur_v):
    visited[cur_v] = True
    print(cur_v, end = " ")

    for new_v in graph[cur_v]:
        if not visited[new_v]:
            dfs(new_v)

dfs(v)
print()

# bfs
visited = [False] * (n + 1)
queue = deque()

visited[v] = True
queue.append(v)
print(v, end = " ")

while queue:
    cur_v = queue.popleft()

    for new_v in graph[cur_v]:
        if not visited[new_v]:
            visited[new_v] = True
            queue.append(new_v)
            print(new_v, end = " ")
