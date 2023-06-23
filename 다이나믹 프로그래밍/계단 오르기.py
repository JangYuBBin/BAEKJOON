# 계단 오르기, 2579번, 백준

# my thoughts :
# 1. By using Dynamic Programming, We can solve it..!!
# 2. dp[i] : i + 1번째 계단을 밟았을 때까지의 점수의 최댓값
# 3. dp[i] = max(dp[i - 2] + arr[i], dp[i - 3] + arr[i - 1] + arr[i])

import sys

n = int(sys.stdin.readline().rstrip())

arr = list()

for _ in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

dp = [0] * n
dp[0] = arr[0]

if n == 1:
    print(dp[0])
    exit()
else:
    pass

dp[1] = arr[0] + arr[1]

if n == 2:
    print(dp[1])
    exit()
else:
    pass

dp[2] = max(arr[0] + arr[2], arr[1] + arr[2])

if n == 3:
    print(dp[2])
    exit()
else:
    pass

for i in range(3, n, 1):
    dp[i] = max(dp[i - 2] + arr[i], dp[i - 3] + arr[i - 1] + arr[i])

print(dp[n - 1])
