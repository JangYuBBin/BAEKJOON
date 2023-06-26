# 점프, 1890번, 백준

# my thoughts :
# 1. By using Dynamic Programming, We can solve it..!!

import sys

n = int(sys.stdin.readline().rstrip())

arr = list()

for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(0, n, 1):
    for j in range(0, n, 1):
        # 오른쪽으로 점프를 하여 (i, j)에 도달하는 경우
        for k in range(0, j, 1):
            if k + arr[i][k] == j:
                dp[i][j] += dp[i][k]
        
        # 아래쪽으로 점프를 하여 (i, j)에 도달하는 경우
        for k in range(0, i, 1):
            if k + arr[k][j] == i:
                dp[i][j] += dp[k][j]

print(dp[n - 1][n - 1])
