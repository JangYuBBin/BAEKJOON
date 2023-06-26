# 상자넣기, 1965번, 백준

# my thoughts :
# 1. By using Dynamic Programming, We can solve it..!!
# 2. 결국 LIS를 찾는 문제입니다..!!

import sys

n = int(sys.stdin.readline().rstrip())

arr = list(map(int, sys.stdin.readline().rstrip().split()))

dp = [1] * n

for i in range(1, n, 1):
    for j in range(0, i, 1):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
