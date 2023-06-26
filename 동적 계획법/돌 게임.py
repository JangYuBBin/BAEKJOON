# 돌 게임, 9655번, 백준

# my thoughts :
# 1. By using Dynamic Programming, We can solve it..!!

import sys

n = int(sys.stdin.readline().rstrip())

dp = [False] * (1_000 + 1)
# 참고1 > dp[i] = True : i번째 돌을 상근이가 가져갔을 경우
# 참고2 > dp[i] = False : i번째 돌을 창영이가 가져갔을 경우

dp[1] = True
dp[2] = False
dp[3] = True

for i in range(4, 1_000 + 1, 1):
    if dp[i - 1] == False:
        dp[i] = True

    if dp[i - 3] == False:
        dp[i] = True

if dp[n] == True:
    print("SK")
else:
    print("CY")
