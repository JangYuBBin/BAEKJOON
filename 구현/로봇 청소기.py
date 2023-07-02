# 로봇 청소기, 14503번, 백준

# my thoughts :
# 1. 까다로웠던 구현 문제인 것 같습니다..!!

import sys
from collections import defaultdict
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())

r, c, d = map(int, sys.stdin.readline().rstrip().split())
start_v = (r, c)

board = list()
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

next = defaultdict(tuple) # <<-- "반시계 방향으로 회전하였을 때 다음 방향은 어디인가..??!!??"
next[0] = [3, 2, 1, 0]
next[1] = [0, 3, 2, 1]
next[2] = [1, 0, 3, 2]
next[3] = [2, 1, 0, 3]

visited = [[False] * m for _ in range(n)]
queue = deque()

visited[start_v[0]][start_v[1]] = True
queue.append((start_v, d))

while queue:
    cur_v, cur_d = queue.popleft()

    checkFlag = False

    for new_d in next[cur_d]:
        if new_d == 0:
            new_v = (cur_v[0] - 1, cur_v[1])
        elif new_d == 1:
            new_v = (cur_v[0], cur_v[1] + 1)
        elif new_d == 2:
            new_v = (cur_v[0] + 1, cur_v[1])
        elif new_d == 3:
            new_v = (cur_v[0], cur_v[1] - 1)
        
        if 0 <= new_v[0] < n and 0 <= new_v[1] < m and board[new_v[0]][new_v[1]] == 0 and not visited[new_v[0]][new_v[1]]:
            visited[new_v[0]][new_v[1]] = True
            queue.append((new_v, new_d))
            
            checkFlag = True
            break
    
    if checkFlag == True:
        pass
    else:
        if cur_d == 0:
            new_v = (cur_v[0] + 1, cur_v[1])
        elif cur_d == 1:
            new_v = (cur_v[0], cur_v[1] - 1)
        elif cur_d == 2:
            new_v = (cur_v[0] - 1, cur_v[1])
        elif cur_d == 3:
            new_v = (cur_v[0], cur_v[1] + 1)
        
        if 0 <= new_v[0] < n and 0 <= new_v[1] < m and board[new_v[0]][new_v[1]] == 0:
            visited[new_v[0]][new_v[1]] = True
            queue.append((new_v, cur_d))

answer = 0

for i in range(0, n, 1):
    for j in range(0, m, 1):
        if visited[i][j]:
            answer += 1
    
print(answer)
