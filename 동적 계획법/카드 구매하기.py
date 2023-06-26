# 카드 구매하기, 11052번, 백준

# my thoughts :
# 1. By using Dynamic Programming, We can solve it..!!
# 2. dp[i] : i개의 카드를 구매하기 위해 민규가 지불해야 할 금액의 최댓값

import sys

n = int(sys.stdin.readline().rstrip())

p = [0] + list(map(int, sys.stdin.readline().rstrip().split()))

dp = [0] * (n + 1)
dp[0] = 0
dp[1] = p[1]

for i in range(2, n + 1, 1):
    for j in range(1, n + 1, 1):
        if i - j >= 0:
            dp[i] = max(dp[i], dp[i - j] + p[j])

print(dp[n])
