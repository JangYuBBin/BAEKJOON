# 가장 긴 감소하는 부분 수열, 11722번, 백준

# my thoughts :
# 1. By using Dynamic Programming, We can solve it..!!
# 2. dp[i] : 인덱스 i까지의 가장 긴 감소하는 부분 수열의 길이

import sys

n = int(sys.stdin.readline().rstrip())

arr = list(map(int, sys.stdin.readline().rstrip().split()))

dp = [1] * (n)

for i in range(1, n, 1):
    for j in range(0, i, 1):
        if arr[i] < arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
