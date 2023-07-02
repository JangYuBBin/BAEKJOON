# 연구소, 14502번, 백준

# my thoughts :
# 1. 일단 빈 칸의 좌표들을 모두 구한다.
# 2. 빈 칸의 좌표들 중에서 3개의 지점을 고른 후 벽을 세우면 된다.
# 3. 3개의 벽을 세운 후 바이러스가 퍼질 수 없는 안전 영역을 구한다.
# 4. 모든 경우에 대한 안전 영역의 최댓값을 구해보자..!!

import sys
from itertools import combinations
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())

board = list()
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

locations_0 = list()
for i in range(0, n, 1):
    for j in range(0, m, 1):
        if board[i][j] == 0:
            locations_0.append((i, j))

cases = list(combinations(locations_0, 3))

answer = list()

for case in cases:
    new_board = [[0] * m for _ in range(n)]
    for i in range(0, n, 1):
        for j in range(0, m, 1):
            new_board[i][j] = board[i][j]

    for i, j in case:
        new_board[i][j] = 1
    
    queue = deque()

    for i in range(0, n, 1):
        for j in range(0, m, 1):
            if new_board[i][j] == 2:
                queue.append((i, j))
    
    while queue:
        cur_v = queue.popleft()

        for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_v = (cur_v[0] + d[0], cur_v[1] + d[1])

            if 0 <= new_v[0] < n and 0 <= new_v[1] < m and new_board[new_v[0]][new_v[1]] == 0:
                new_board[new_v[0]][new_v[1]] = 2
                queue.append(new_v)

    cnt = 0 # <<-- "해당 경우에 대한 안전영역의 크기입니다..!!"

    for i in range(0, n, 1):
        for j in range(0, m, 1):
            if new_board[i][j] == 0:
                cnt += 1
    
    answer.append(cnt)

answer.sort(reverse = True)

print(answer[0])
