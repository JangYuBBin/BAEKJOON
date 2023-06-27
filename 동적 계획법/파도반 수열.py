# 파도반 수열, 9461번, 백준

# my thoughts :
# 1. By using Dynamic Programming, We can solve it..!!
# 2. dp[i] : i번째 삼각형의 한 변의 길이
# 3. dp[i] = dp[i - 1] + dp[i - 5]

import sys

dp = [0] * (100 + 1)
dp[0] = 0
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2

for i in range(6, 100 + 1, 1):
    dp[i] = dp[i - 1] + dp[i - 5]

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())

    print(dp[n])
