# 타일 채우기, 2133번, 백준 

# my thoughts :
# 1. By using Dynamic Programming, We can solve it..!!
# 2. dp[n] = 3 * dp[n - 2] + 2 * (dp[n - 4] + dp[n - 6] + .... + dp[0])
# 3. 또한 n이 홀수일 때 dp[n] = 0임..!!

import sys

n = int(sys.stdin.readline().rstrip())

dp = [0] * (30 + 1)
dp[0] = 1
dp[2] = 3

for i in range(4, 30 + 1, 2):
    dp[i] += dp[i - 2] * 3

    for j in range(4, i + 1, 2):
        dp[i] += dp[i - j] * 2

print(dp[n])
