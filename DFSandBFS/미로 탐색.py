# 미로 탐색, 2178번, 백준

# my thoughts :
# 1. By using BFS, We can solve it..!!

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())

board = list()

for _ in range(n):
    board.append(sys.stdin.readline().rstrip())

visited = [[False] * len(board[0]) for _ in range(len(board))]
queue = deque()

visited[0][0] = True
queue.append((1, (0, 0)))

while queue:
    cur_cnt, cur_v = queue.popleft()

    if cur_v == (n - 1, m - 1):
        print(cur_cnt)
        exit()

    for d in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
        new_v = (cur_v[0] + d[0], cur_v[1] + d[1])

        if 0 <= new_v[0] < n and 0 <= new_v[1] < m and board[new_v[0]][new_v[1]] == "1" and not visited[new_v[0]][new_v[1]]:
            visited[new_v[0]][new_v[1]] = True
            queue.append((cur_cnt + 1, new_v))
