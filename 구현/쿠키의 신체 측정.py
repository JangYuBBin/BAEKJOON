# 쿠키의 신체 측정, 20125번, 백준

# my thoughts :
# 1. 일단 심장의 위치를 찾아야 합니다.
# 2. 심장의 위치는 심장의 위치를 (i, j)라고 하였을 때 상, 하, 좌, 우 칸 모두 *표시 되어있는 칸이라고 할 수 있습니다.
# 3. 심장의 위치를 구했다면 왼쪽 팔과 오른쪽 팔의 길이를 구합니다.
# 4. 그런다음 허리의 길이를 구합니다.
# 5. 그런다음 왼쪽 다리와 오른쪽 다리의 길이를 구합니다.

import sys

n = int(sys.stdin.readline().rstrip())

board = list()
for _ in range(n):
    board.append(list(sys.stdin.readline().rstrip()))

# 일단 심장의 위치를 먼저 찾아냅시다..!!
heart = [0, 0]

for i in range(1, n - 1, 1):
    for j in range(1, n - 1, 1):
        if board[i - 1][j] == board[i][j + 1] == board[i + 1][j] == board[i][j - 1] == "*":
            heart = [i, j]
            break

# 그다음으로 왼쪽 팔의 길이를 구합시다..!!
left_hand = 0

for j in range(heart[1] - 1, -1, -1):
    if board[heart[0]][j] == "*":
        left_hand += 1
    else:
        break

# 그다음으로 오른쪽 팔의 길이를 구합시다..!!
right_hand = 0

for j in range(heart[1] + 1, n, 1):
    if board[heart[0]][j] == "*":
        right_hand += 1
    else:
        break

# 그다음으로 허리의 길이를 구해봅시다..!! -->> 허리의 길이를 구하는 대신 허리가 끝나는 지점을 먼저 구해봅시다..!!
heori_end = [0, 0]

for i in range(heart[0] + 1, n, 1):
    if board[i][heart[1]] == "*":
        heori_end = [i, heart[1]]

heori = heori_end[0] - heart[0]

# 그다음으로 왼쪽 다리의 길이를 구해봅시다..!!
left_leg_start = [heori_end[0] + 1, heori_end[1] - 1]
left_leg_end = [heori_end[0] + 1, heori_end[1] - 1]

for i in range(left_leg_start[0] + 1, n, 1):
    if board[i][left_leg_start[1]] == "*":
        left_leg_end[0] = i

left_leg = left_leg_end[0] - left_leg_start[0] + 1

# 그다음으로 오른쪽 다리의 길이를 구해봅시다..!!
right_leg_start = [heori_end[0] + 1, heori_end[1] + 1]
right_leg_end = [heori_end[0] + 1, heori_end[1] + 1]

for i in range(right_leg_start[0] + 1, n, 1):
    if board[i][right_leg_start[1]] == "*":
        right_leg_end[0] = i

right_leg = right_leg_end[0] - right_leg_start[0] + 1

print(heart[0] + 1, heart[1] + 1)
print(left_hand, right_hand, heori, left_leg, right_leg)
