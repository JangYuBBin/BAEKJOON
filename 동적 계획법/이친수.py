# 이친수, 2193번, 백준

# my thoughts :
# 1. By using Dynamic Programming, We can solve it..!!
# 2. dp[i][0] : 길이가 i이면서 0으로 끝나는 이친수의 갯수
# 3. dp[i][1] : 길이가 i이면서 1로 끝나는 이친수의 갯수
# 4. dp[i][0] = dp[i - 1][0] + dp[i - 1][1]
# 5. dp[i][1] = dp[i - 1][0]

import sys

n = int(sys.stdin.readline().rstrip())

dp = [[0] * 2 for _ in range(n + 1)]
dp[1][0] = 0
dp[1][1] = 1

for i in range(2, n + 1, 1):
    dp[i][0] = dp[i - 1][0] + dp[i - 1][1]
    
    dp[i][1] = dp[i - 1][0]

print(sum(dp[n]))
