# 구간 합 구하기 5, 11660번, 백준

# my thoughts :
# 1. By using Dynamic Programming, We can solve it..!!

import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

arr = list()

for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

dp = [[0] * n for _ in range(n)]
# dp[i][j] : (0, 0)에서부터 (i, j)까지의 합

dp[0][0] = arr[0][0]

for i in range(0, 1, 1):
    for j in range(1, n, 1):
        dp[i][j] = dp[i][j - 1] + arr[i][j]

for i in range(1, n, 1):
    for j in range(0, 1, 1):
        dp[i][j] = dp[i - 1][j] + arr[i][j]

for i in range(1, n, 1):
    for j in range(1, n, 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + arr[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())

    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1

    answer = dp[x2][y2]

    if x1 - 1 < 0:
        pass
    else:
        answer -= dp[x1 - 1][y2]
    
    if y1 - 1 < 0:
        pass
    else:
        answer -= dp[x2][y1 - 1]
    
    if x1 - 1 < 0 or y1 - 1 < 0:
        pass
    else:
        answer += dp[x1 - 1][y1 - 1]
    
    print(answer)
