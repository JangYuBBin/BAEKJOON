# 가장 긴 증가하는 부분 수열 4, 14002번, 백준

# my thoughts :
# 1. By using Dynamic Programming, We can solve it..!!
# 2. dp[i] : 인덱스 i까지의 가장 긴 증가하는 부분 수열
# 3. ....

import sys

n = int(sys.stdin.readline().rstrip())

arr = list(map(int, sys.stdin.readline().rstrip().split()))

dp = [[] for _ in range(n)]

for i in range(0, n, 1):
    dp[i] = [arr[i]]

for i in range(1, n, 1):
    for j in range(0, i, 1):
        if arr[i] > arr[j]:
            if len(dp[i]) < len(dp[j]) + 1:
                dp[i] = dp[j] + [arr[i]]

answer_len = 0
answer_list = []

for i in range(0, n, 1):
    if len(dp[i]) > answer_len:
        answer_len = len(dp[i])
        answer_list = dp[i]

print(answer_len)
for val in answer_list:
    print(val, end = " ")
