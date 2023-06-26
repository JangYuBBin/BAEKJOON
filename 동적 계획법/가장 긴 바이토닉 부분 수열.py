# 가장 긴 바이토닉 부분 수열, 11054번, 백준

# my thoughts :
# 1. By using Dynamic Programming, We can solve it..!!
# 2. 인덱스 i의 값을 Sk라 할때 가장 긴 바이토닉 부분 수열의 길이(은)는 인덱스 i까지 가장 긴 증가하는 부분 수열의 길이 + 인덱스 i부터 가장 긴 감소하는 부분 수열의 길이 - 1이다.
# 3. 일단 해보자..!!

import sys

n = int(sys.stdin.readline().rstrip())

arr = list(map(int, sys.stdin.readline().rstrip().split()))

dp1 = [1] * n
# dp1[i] : 인덱스 i까지의 가장 긴 증가하는 부분 수열의 길이

for i in range(1, n, 1):
    for j in range(0, i, 1):
        if arr[i] > arr[j]:
            dp1[i] = max(dp1[i], dp1[j] + 1)

dp2 = [1] * n
# dp2[i] : 인덱스 i부터 가장 긴 감소하는 부분 수열의 길이

for i in range(n - 2, -1, -1):
    for j in range(n - 1, i, -1):
        if arr[i] > arr[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)

answer = 0

for i in range(0, n, 1):
    if answer < dp1[i] + dp2[i] - 1:
        answer = dp1[i] + dp2[i] - 1

print(answer)
