# RGB거리, 1149번, 백준

# my thoughts :
# 1. By using Dynamic Programming, We can solve it..!!
# 2. dp[i][0] : i번째 집을 빨강색으로 칠했을 때 발생하는 비용의 최솟값
# 3. dp[i][1] : i번째 집을 초록색으로 칠했을 때 발생하는 비용의 최솟값
# 4. dp[i][2] : i번째 집을 파랑색으로 칠했을 때 발생하는 비용의 최솟값

import sys

n = int(sys.stdin.readline().rstrip())

arr = list()

for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

dp = [[0] * 3 for _ in range(n)]
dp[0][0] = arr[0][0]
dp[0][1] = arr[0][1]
dp[0][2] = arr[0][2]

for i in range(1, n, 1):
    dp[i][0] = min(dp[i - 1][1] , dp[i - 1][2]) + arr[i][0]

    dp[i][1] = min(dp[i - 1][0] , dp[i - 1][2]) + arr[i][1]

    dp[i][2] = min(dp[i - 1][0] , dp[i - 1][1]) + arr[i][2]

print(min(dp[n - 1]))
