# 동전 2, 2294번, 백준

# my thoughts :
# 1. By using Dynamic Programming, We can solve it..!!

import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

coins = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
coins.sort()

dp = [float("inf")] * (k + 1)
dp[0] = 0
# 참고 > dp[i] : i원의 가치를 만드는데 필요한 동전의 최소 갯수

for i in range(1, k + 1, 1):
    for coin in coins:
        if i - coin >= 0:
            dp[i] = min(dp[i], dp[i - coin] + 1)
        else:
            break

if dp[k] == float("inf"):
    print(-1)
else:
    print(dp[k])
