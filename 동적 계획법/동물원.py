# 동물원, 1309번, 백준

# my thoughts :
# 1. By using Dynamic Programming, We can solve it..!!
# 2. dp[i][0] : 추가로 2 x 1 배열을 추가할 때 첫번째 칸에 사자를 배치하는 경우
# 3. dp[i][1] : 추가로 2 x 1 배열을 추가할 때 두번째 칸에 사자를 배치하는 경우
# 4. dp[i][2] : 추가로 2 x 1 배열을 추가할 때 사자를 배치하지 않는 경우
# 5. dp[i][0] = dp[i - 1][1] + dp[i - 1][2]
# 6. dp[i][1] = dp[i - 1][0] + dp[i - 1][2]
# 7. dp[i][2] = dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]
# 8. 추가로 메모리 초과 판정을 피하기 위해서 모듈러 연산을 활용합시다..!!

import sys

n = int(sys.stdin.readline().rstrip())

dp = [[0] * 3 for _ in range(2)]
dp[1][0] = 1
dp[1][1] = 1
dp[1][2] = 1

for i in range(2, n + 1, 1):
    dp[i % 2][0] = dp[(i - 1) % 2][1] + dp[(i - 1) % 2][2]
    dp[i % 2][0] %= 9901

    dp[i % 2][1] = dp[(i - 1) % 2][0] + dp[(i - 1) % 2][2]
    dp[i % 2][1] %= 9901

    dp[i % 2][2] = dp[(i - 1) % 2][0] + dp[(i - 1) % 2][1] + dp[(i - 1) % 2][2]
    dp[i % 2][2] %= 9901

print(sum(dp[n % 2]) % 9901)
