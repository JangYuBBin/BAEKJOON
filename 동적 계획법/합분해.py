# 합분해, 2225번, 백준

# my thoughts :
# 1. By using Dynamic Programming, We can solve it..!!
# 2. dp[i][j] : 정수 i개를 더해서 합이 j가 되는 경우의 수
# 3. dp[i][j] = dp[i - 1][0] + dp[i - 1][1] + .... + dp[i - 1][j]
# 4. (ex) dp[2][3] = dp[1][0] + dp[1][1] + dp[1][2] + dp[1][3]

import sys

N, K = map(int, sys.stdin.readline().rstrip().split())

dp = [[0] * (N + 1) for _ in range(K + 1)]
for i in range(1, 1 + 1, 1):
    for j in range(0, N + 1, 1):
        dp[i][j] = 1 # 초깃값 설정

for i in range(2, K + 1, 1):
    for j in range(0, N + 1, 1):
        for k in range(0, j + 1, 1):
            dp[i][j] += dp[i - 1][k]
            dp[i][j] %= 1_000_000_000

print(dp[K][N] % 1_000_000_000)
