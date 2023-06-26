# 동전 1, 2293번, 백준

# my thoughts :
# 1. By using Dynamic Programming, We can solve it..!!

import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

coins = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
coins.sort()

dp = [0] * (k + 1)
# dp[i] : i원을 나타내는 경우의 수
dp[0] = 1

for coin in coins:
    for i in range(1, k + 1, 1):
        if i - coin >= 0:
            dp[i] += dp[i - coin]

print(dp[k])
