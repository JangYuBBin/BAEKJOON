# 이동하기, 11048번, 백준

# my thoughts :
# 1. By using Dynamic Programming, We can solve it..!!
# 2. dp[i][j] : (i, j)까지 이동했을 때 얻을 수 있는 사탕의 최대 갯수
# 3. dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + arr[i][j]
# 4. 물론 예외 상황도 고려해주어야 합니다..!!

import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

arr = list()

for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

dp = [[0] * m for _ in range(n)]
dp[0][0] = arr[0][0]

for i in range(0, 0 + 1, 1):
    for j in range(1, m, 1):
        dp[i][j] = dp[i][j - 1] + arr[i][j]

for i in range(1, n, 1):
    for j in range(0, 0 + 1, 1):
        dp[i][j] = dp[i - 1][j] + arr[i][j]

for i in range(1, n, 1):
    for j in range(1, m, 1):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + arr[i][j]

print(dp[n - 1][m - 1])
