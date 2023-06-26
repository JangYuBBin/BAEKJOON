# 평범한 배낭, 12865번, 백준

# my thoughts :
# 1. 틀렸던 문제이고 어려운 문제이므로 다음에 다시 풀면 좋을 듯 합니다..!!
# 2. dp[i][j] : i번째 인덱스의 물건까지 확인했을 때 무게제한이 j인 가방에 담을 수 있는 물건들의 가치의 최대합
# 3. 그렇다면 결국 우리가 구해야 하는 것은 dp[n - 1][k]입니다.

import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

arr = list()

for _ in range(n):
    w, v = map(int, sys.stdin.readline().rstrip().split())

    arr.append((w, v))

dp = [[0] * (k + 1) for _ in range(n)]

for i in range(0, n, 1):
    w = arr[i][0] # 현재 확인하고 있는 물건의 무게
    v = arr[i][1] # 현재 확인하고 있는 물건의 가치

    for j in range(0, k + 1, 1):
        if j < w:
            dp[i][j] = dp[i - 1][j]
        elif j >= w:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)

print(dp[n - 1][k])
