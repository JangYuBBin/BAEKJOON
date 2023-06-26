# 전깃줄, 2565번, 백준

# my thoughts :
# 1. 어렵고 틀린 문제이므로 나중에 다시 풀어보면 좋을 문제인듯 합니다.
# 2. 제거해야 할 전깃줄을 찾지말고 오히려 거꾸로 남길 전깃줄의 최대갯수를 찾으면 되는 것입니다.
# 3. 즉, LIS(최장 증가 부분 수열)를 찾으면 되는 문제라고 할 수 있습니다..!!

import sys

n = int(sys.stdin.readline().rstrip())

arr = list()

for _ in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())

    arr.append((a, b))

arr.sort(key = lambda x : x[0], reverse = False)

# print(arr)
# 출력결과 Ex : [(1, 8), (2, 2), (3, 9), (4, 1), (6, 4), (7, 6), (9, 7), (10, 10)]

dp = [1] * (n)

for i in range(1, n, 1):
    for j in range(0, i, 1):
        if arr[i][1] > arr[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
