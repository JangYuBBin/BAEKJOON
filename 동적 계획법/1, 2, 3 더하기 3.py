# 1, 2, 3 더하기 3, 15988번, 백준

# my thoughts :
# 1. By using Dynamic Programming, We can solve it..!!

import sys

dp = [0] * 1_000_001
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 1_000_001, 1):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    dp[i] %= 1_000_000_009

for _ in range(int(sys.stdin.readline().rstrip())):
    print(dp[int(sys.stdin.readline().rstrip())])
