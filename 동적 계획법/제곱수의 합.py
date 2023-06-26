# 제곱수의 합, 1699번, 백준

# my thoughts :
# 1. By using Dynamic Programming, We can solve it..!!
# 2. 먼저 N의 범위가 100_000이하이므로 100_000이하의 제곱수들을 모두 구해논다.
# 3. ....

import sys

n = int(sys.stdin.readline().rstrip())

nums = list() # <<-- "100_000이하의 제곱수들을 모두 모아논 1차원 리스트의 선언입니다..!!"

for i in range(1, 100_000 + 1, 1):
    val = i**2

    if val > 100_000:
        break
    else:
        nums.append(val)

dp = [float("inf")] * (n + 1)
# dp[i] : 합이 i이면서 제곱수의 합으로 표현했을 때 제곱수 항의 최소 갯수
dp[0] = 0
dp[1] = 1

for i in range(1, n + 1, 1):
    for num in nums:
        if i - num >= 0:
            dp[i] = min(dp[i], dp[i - num] + 1)
        else:
            break

print(dp[n])
