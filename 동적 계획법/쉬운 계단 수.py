# 쉬운 계단 수, 10844번, 백준

# my thoughts :
# 1. By using Dynamic Programming, We can solve it..!!
# 2. dp[i][j] : 길이가 i이면서 숫자 j로 끝나는 계단 수의 가짓수
# 3. dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
# 4. 당연히 예외 경우도 고려해주어야 합니다..!!

import sys

n = int(sys.stdin.readline().rstrip())

dp = [[0] * 10 for _ in range(n + 1)]
dp[1][1] = dp[1][2] = dp[1][3] = dp[1][4] = dp[1][5] = dp[1][6] = dp[1][7] = dp[1][8] = dp[1][9] = 1
dp[1][0] = 0 # <<-- "0으로 시작하는 수는 계단 수가 아니다."

for i in range(2, n + 1, 1):
    for j in range(0, 10, 1):
        if j == 0:
            dp[i][j] = dp[i - 1][j + 1]
            dp[i][j] %= 1_000_000_000
        elif j == 9:
            dp[i][j] = dp[i - 1][j - 1]
            dp[i][j] %= 1_000_000_000
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
            dp[i][j] %= 1_000_000_000

print(sum(dp[n]) % 1_000_000_000)
