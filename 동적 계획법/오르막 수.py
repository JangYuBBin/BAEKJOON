# 오르막 수, 11057번, 백준

# my thoughts :
# 1. By using Dynamic Programming, We can solve it..!!
# 2. dp[i][j] : 길이가 i이면서 j로 끝나는 오르막 수의 갯수

import sys

n = int(sys.stdin.readline().rstrip())

dp = [[0] * 10 for _ in range(n + 1)]
dp[1][0] = 1
dp[1][1] = 1
dp[1][2] = 1
dp[1][3] = 1
dp[1][4] = 1
dp[1][5] = 1
dp[1][6] = 1
dp[1][7] = 1
dp[1][8] = 1
dp[1][9] = 1

for i in range(2, n + 1, 1):
    for j in range(0, 9 + 1, 1):
        for k in range(0, j + 1, 1):
            dp[i][j] += dp[i - 1][k]
            dp[i][j] %= 10_007

print(sum(dp[n]) % 10_007)
