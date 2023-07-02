# 색종이, 2563번, 백준

import sys

board = [[False] * 100 for _ in range(100)]

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())

    for i in range(x, x + 10, 1):
        for j in range(y, y + 10, 1):
            board[i][j] = True

answer = 0

for i in range(0, 100, 1):
    for j in range(0, 100, 1):
        if board[i][j] == True:
            answer += 1

print(answer)
