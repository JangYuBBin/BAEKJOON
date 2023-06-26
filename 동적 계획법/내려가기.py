# 내려가기, 2096번, 백준

# my thoughts :
# 1. By using Dynamic Programming, We can solve it..!!
# 2. 또한 메모리 제한이 4MB이기 때문에 약간의 로직이 더 필요한 문제였습니다..!!

import sys

n = int(sys.stdin.readline().rstrip())

arr = list()

for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

# 먼저 최대 점수를 구해봅시다..!!
dp = [[0] * 3 for _ in range(2)]
dp[0][0] = arr[0][0]
dp[0][1] = arr[0][1]
dp[0][2] = arr[0][2]

for i in range(1, n, 1):
    dp[i % 2][0] = max(dp[(i - 1) % 2][0], dp[(i - 1) % 2][1]) + arr[i][0]

    dp[i % 2][1] = max(dp[(i - 1) % 2][0], dp[(i - 1) % 2][1], dp[(i - 1) % 2][2]) + arr[i][1]

    dp[i % 2][2] = max(dp[(i - 1) % 2][1], dp[(i - 1) % 2][2]) + arr[i][2]

print(max(dp[(n - 1) % 2]), end = " ")

# 이제 최소 점수를 구해봅시다..!!
dp[0][0] = arr[0][0]
dp[0][1] = arr[0][1]
dp[0][2] = arr[0][2]

for i in range(1, n, 1):
    dp[i % 2][0] = min(dp[(i - 1) % 2][0], dp[(i - 1) % 2][1]) + arr[i][0]

    dp[i % 2][1] = min(dp[(i - 1) % 2][0], dp[(i - 1) % 2][1], dp[(i - 1) % 2][2]) + arr[i][1]

    dp[i % 2][2] = min(dp[(i - 1) % 2][1], dp[(i - 1) % 2][2]) + arr[i][2]

print(min(dp[(n - 1) % 2]))
