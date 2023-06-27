# 전깃줄, 2565번, 백준

# my thoughts :
# 1. 거꾸로 생각해봅시다.
# 2. 없애야 하는 전깃줄의 최소 갯수를 찾지 말고 남아야 하는 전깃줄의 최대 갯수를 찾아봅시다.
# 3. 즉 LIS(Longest Increasing Subsequence)를 찾는 문제입니다..!!

import sys

n = int(sys.stdin.readline().rstrip())

arr = list()

for _ in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())

    arr.append((a, b))

arr.sort(key = lambda x : x[0], reverse = False)

dp = [1] * (n)
# 참고 > dp[i] : 인덱스 i까지 확인하였을 때 가장 긴 증가하는 부분 수열의 길이

for i in range(1, n, 1):
    for j in range(0, i, 1):
        if arr[i][1] > arr[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
