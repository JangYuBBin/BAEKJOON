# 1, 2, 3 더하기, 9095번, 백준

# my thoughts :
# 1. By using Dynamic Programming, We can solve it..!!

import sys

dp = [0] * (11)
dp[0] = 1

for i in range(1, 11, 1):
    for num in [1, 2, 3]:
        if i - num >= 0:
            dp[i] += dp[i - num]

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())

    print(dp[n])
