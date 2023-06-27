# 연속합, 1912번, 백준

# my thoughts :
# 1. By using Dynamic Programming, We can solve it..!!
# 2. dp[i] : 인덱스 i까지의 가장 큰 합
# 3. dp[i] = max(arr[i], dp[i - 1] + arr[i])

import sys

n = int(sys.stdin.readline().rstrip())

arr = list(map(int, sys.stdin.readline().rstrip().split()))

dp = [0] * (n)
dp[0] = arr[0]

for i in range(1, n, 1):
    dp[i] = max(arr[i], dp[i - 1] + arr[i])
    
print(max(dp))
