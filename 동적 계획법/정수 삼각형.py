# 정수 삼각형, 1932번, 백준

# my thoughts :
# 1. By using Dynamic Programming, We can solve it..!!
# 2. 각 행의 0열에서의 dp[i][0] = dp[i - 1][0] + arr[i][0]
# 3. 각 행의 마지막열에서의 dp[i][i] = dp[i - 1][i - 1] + arr[i][i]
# 4. 각 행의 그 밖의 열에서의 dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + arr[i][j]

import sys

n = int(sys.stdin.readline().rstrip())

arr = list()

for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

dp = [[0] * n for _ in range(n)]
dp[0][0] = arr[0][0]

for i in range(1, n, 1):
    dp[i][0] = dp[i - 1][0] + arr[i][0]

    for j in range(1, i, 1):
        dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + arr[i][j]
    
    dp[i][i] = dp[i - 1][i - 1] + arr[i][i]

print(max(dp[n - 1]))
