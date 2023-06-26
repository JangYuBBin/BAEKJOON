# 1로 만들기 2, 12852번, 백준

# my thoughts :
# 1. By using Dynamic Programming, We can solve it..!!
# 2. n에서 1로 가는 방식이 아닌 1에서 n으로 가는 방식으로 문제에 접근해봅시다..!!
# 2. dp[i] : i까지 만드는 데 필요한 최소 횟수
# 3. parent[j] = i : j까지 만드는 데 연산을 최소한을 사용하려면 i에서 j로 만들어야 한다는 의미입니다..!!

import sys

n = int(sys.stdin.readline().rstrip())

dp = [float("inf")] * (n + 1)
parent = [0] * (n + 1)

dp[1] = 0
parent[1] = 1

for i in range(2, n + 1, 1):
    if i % 3 == 0:
        if dp[i] > dp[i // 3] + 1:
            dp[i] = dp[i // 3] + 1
            parent[i] = i // 3

    if i % 2 == 0:
        if dp[i] > dp[i // 2] + 1:
            dp[i] = dp[i // 2] + 1
            parent[i] = i // 2
    
    if dp[i] > dp[i - 1] + 1:
        dp[i] = dp[i - 1] + 1
        parent[i] = i - 1

print(dp[n])

path = list()
path.append(n)

while parent[path[-1]] != path[-1]:
    path.append(parent[path[-1]])

for val in path:
    print(val, end = " ")
