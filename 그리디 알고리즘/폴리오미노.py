# 폴리오미노, 1343번, 백준

# my thoughts :
# 1. 사전순으로 앞서는 답을 출력해야 하므로 4칸이 비어있다면 AAAA를 집어넣어야 합니다.
# 2. ....

import sys

board = list(sys.stdin.readline().rstrip())

for i in range(0, len(board) - 1, 1):
    if board[i] == ".":
        continue
    elif i + 3 <= len(board) - 1 and board[i] == board[i + 1] == board[i + 2] == board[i + 3] == "X":
        board[i] = "A"
        board[i + 1] = "A"
        board[i + 2] = "A"
        board[i + 3] = "A"
    elif i + 1 <= len(board) - 1 and board[i] == board[i + 1] == "X":
        board[i] = "B"
        board[i + 1] = "B"

for i in range(0, len(board), 1):
    if board[i] == "X":
        print(-1)
        exit()

answer = "".join(board)

print(answer)
