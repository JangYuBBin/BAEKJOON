# 치킨 배달, 15686번, 백준

import sys
from itertools import combinations
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())

board = list()
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

chickens = list()# <<-- "현재 존재하는 치킨집의 좌표들을 담을 리스트의 선언입니다..!!"

for i in range(0, n, 1):
    for j in range(0, n, 1):
        if board[i][j] == 2:
            chickens.append((i, j))

cases = list(combinations(chickens, m))

answer = list()

for case in cases:
    new_board = [[0] * n for _ in range(n)]
    new_chickens = case

    for i in range(0, n, 1):
        for j in range(0, n, 1):
            if board[i][j] == 1:
                new_board[i][j] = 1
    
    for i, j in new_chickens:
        new_board[i][j] = 2
    
    distance = 0 # <<-- "도시의 치킨 거리..!!"

    for i in range(0, n, 1):
        for j in range(0, n, 1):
            if board[i][j] == 1:
                diff = float("inf")

                for l, m in new_chickens:
                    if diff > abs(l - i) + abs(m - j):
                        diff = abs(l - i) + abs(m - j)
                
                distance += diff
    
    answer.append(distance)

answer.sort()

print(answer[0])
