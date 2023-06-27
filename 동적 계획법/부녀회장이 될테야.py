# 부녀회장이 될테야, 2775번, 백준

# my thoughts :
# 1. By using Dynamic Programming, We can solve it..!!
# 2. dp[0][1] = 1, dp[0][2] = 2, dp[0][3] = 3, ....
# 3. dp[i][j] = dp[i - 1][1] + .... + dp[i - 1][j]

import sys

dp = [[0] * (14 + 1) for _ in range(14 + 1)]
for i in range(0, 0 + 1, 1):
    for j in range(1, 14 + 1, 1):
        dp[i][j] = j

for i in range(1, 14 + 1, 1):
    for j in range(1, 14 + 1, 1):
        for k in range(1, j + 1, 1):
            dp[i][j] += dp[i - 1][k]

for _ in range(int(sys.stdin.readline().rstrip())):
    k = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())

    print(dp[k][n])
