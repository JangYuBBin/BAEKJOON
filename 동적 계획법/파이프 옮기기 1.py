# 파이프 옮기기 1, 17070번, 백준

# my thoughts :
# 1. By using Dynamic Programming, We can solve it..!!
# 2. 3차원 Dp배열로 문제에 접근하면 될 것입니다..!!
# 3. dp[i][j][0] = 가로 모양으로 (i, j)에 도착하는 경우
# 4. dp[i][j][1] = 세로 모양으로 (i, j)에 도착하는 경우
# 5. dp[i][j][2] = 대각선 모양으로 (i, j)에 도착하는 경우
# 6. 다음에 다시 풀어보면 좋을 문제인 것 같습니다..!!

import sys

n = int(sys.stdin.readline().rstrip())

arr = list()

for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]
# 초깃값 셋팅
dp[0][1][0] = 1
dp[0][1][1] = 0
dp[0][1][2] = 0

for i in range(0, n, 1):
    for j in range(0, n, 1):
        if arr[i][j] == 1: # <<-- "현재 확인하고 있는 칸이 벽으로 이루어져있다면 갈 수 없는 칸이기 때문입니다..!!"
            continue
        else:
            pass

        # 1. 가로상태로 (i, j)에 도착하는 경우
        # 1-1. 가로상태 -->> 가로상태로 가는 경우
        if 0 <= i < n and 0 <= j - 1 < n:
            dp[i][j][0] += dp[i][j - 1][0]
        # 1-2. 대각선상태 -->> 가로상태로 가는 경우
        if 0 <= i < n and  0 <= j - 1 < n:
            dp[i][j][0] += dp[i][j - 1][2]
        
        # 2. 세로상태로 (i, j)에 도착하는 경우
        # 2-1. 세로상태 -->> 세로상태로 가는 경우
        if 0 <= i - 1 < n and 0 <= j < n:
            dp[i][j][1] += dp[i - 1][j][1]
        # 2-2. 대각선상태 -->> 세로상태로 가는 경우
        if 0 <= i - 1 < n and 0 <= j < n:
            dp[i][j][1] += dp[i - 1][j][2]
        
        # 3. 대각선상태로 (i, j)에 가는 경우
        # 3-1. 가로상태 -->> 대각선상태로 가는 경우
        if 0 <= i - 1 < n and 0 <= j - 1 < n and arr[i - 1][j] == arr[i][j - 1] == 0:
            dp[i][j][2] += dp[i - 1][j - 1][0]
        # 3-2. 세로상태 -->> 대각선상태로 가는 경우
        if 0 <= i - 1 < n and 0 <= j - 1 < n and arr[i - 1][j] == arr[i][j - 1] == 0:
            dp[i][j][2] += dp[i - 1][j - 1][1]
        # 3-3. 대각선상태 -->> 대각선상태로 가는 경우
        if 0 <= i - 1 < n and 0 <= j - 1 < n and arr[i - 1][j] == arr[i][j - 1] == 0:
            dp[i][j][2] += dp[i - 1][j - 1][2]

print(dp[n - 1][n - 1][0] + dp[n - 1][n - 1][1] + dp[n - 1][n - 1][2])
