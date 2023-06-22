# 설탕 배달, 2839번, 백준

# my thoughts :
# 1. By using Dynamic Programming, We can solve it..!!

import sys

n = int(sys.stdin.readline().rstrip())

dp = [float("inf")] * (n + 1)
dp[0] = 0

for i in range(3, n + 1, 1):
    if i - 3 >= 0:
        dp[i] = min(dp[i], dp[i - 3] + 1)
    
    if i - 5 >= 0:
        dp[i] = min(dp[i], dp[i - 5] + 1)

if dp[n] == float("inf"):
    print(-1)
else:
    print(dp[n])
