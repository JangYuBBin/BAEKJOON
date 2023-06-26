# 01타일, 1904번, 백준

# my thoughts :
# 1. By using Dynamic Programming, We can solve it..!!

import sys

n = int(sys.stdin.readline().rstrip())

dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 1

if n == 1:
    print(dp[1])
    exit()
else:
    pass

for i in range(2, n + 1, 1):
    dp[i] = dp[i - 1] + dp[i - 2]
    dp[i] %= 15746

print(dp[n])
