# 이항 계수 2, 11051번, 백준

# my thoughts :
# 1. By using Dynamic Programming, We can solve it..!!
# 2. 이런 문제는 알맞은 점화식을 찾는 것이 가장 중요하다.
# 3. nCk = n-1Ck-1 + n-1Ck
# 4. dp[n][k] = nCk
# 5. dp[n][k] = dp[n - 1][k - 1] + dp[n - 1][k]

import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

dp = [[0] * (n + 1) for _ in range(n + 1)]
dp[1][0] = 1
dp[1][1] = 1

for i in range(2, n + 1, 1):
    for j in range(0, i + 1, 1):
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        dp[i][j] %= 10_007

print(dp[n][k])
