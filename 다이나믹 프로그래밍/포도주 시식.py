# 포도주 시식, 2156번, 백준

# my thoughts :
# 1. By using Dynamic Programming, We can solve it..!!
# 2. dp[i] : 인덱스 i까지의 마실 수 있는 포도주 양의 합의 최댓값
# 3. dp[i] = max(dp[i - 1], dp[i - 2] + arr[i], dp[i - 3] + arr[i - 1] + arr[i])

import sys

n = int(sys.stdin.readline().rstrip())

arr = [0]

for _ in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

dp = [0] * (n + 1)
dp[1] = arr[1]

if n == 1:
    print(dp[1])
    exit()
else:
    pass

dp[2] = arr[1] + arr[2]

if n == 2:
    print(dp[2])
    exit()
else:
    pass

for i in range(3, n + 1, 1):
    dp[i] = max(dp[i - 1], dp[i - 2] + arr[i], dp[i - 3] + arr[i - 1] + arr[i])

print(dp[n])
