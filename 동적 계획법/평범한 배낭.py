# 평범한 배낭, 12865번, 백준

# my thoughts :
# 1. 아주 유명한 냅색 문제(Knapsack Problem) or 0 - 1 배낭문제라고 합니다.
# 2. By using Dynamic Programming, We can solve it..!!
# 3. dp[i][j] : i번째 물건까지 확인하였을 때 무게제한이 j인 가방에 들어갈 수 있는 물건들의 가치합의 최대합
# 4. 결국 우리가 구해야 하는 것은 dp[n][k]입니다..!!
# 5. 다음에 다시 풀어보면 좋을 문제인 것 같습니다..!!

import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

arr = [(0, 0)]

for _ in range(n):
    w, v = map(int, sys.stdin.readline().rstrip().split())

    arr.append((w, v))

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1, 1):
    w = arr[i][0] # 현재 확인하고 있는 물건의 무게
    v = arr[i][1] # 현재 확인하고 있는 물건의 가치

    for j in range(0, k + 1, 1):
        if j < w:
            dp[i][j] = dp[i - 1][j]
        elif j >= w:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)

print(dp[n][k])
