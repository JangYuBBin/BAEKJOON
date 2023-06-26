# 스티커, 9465번, 백준

# my thoughts :
# 1. By using Dynamic Programming, We can solve it..!!
# 2. dp[0][i] : i열까지 확인했을 때 i열의 위쪽 스티커를 떼는 경우
# 3. dp[1][i] : i열까지 확인했을 때 i열의 아래쪽 스티커를 떼는 경우
# 4. dp[2][i] : i열까지 확인했을 때 i열의 스티커를 떼지 않는 경우

import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())

    arr = list()

    for _ in range(2):
        arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

    dp = [[0] * n for _ in range(3)]
    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]
    dp[2][0] = 0

    for i in range(1, n, 1):
        dp[0][i] = max(dp[1][i - 1], dp[2][i - 1]) + arr[0][i]

        dp[1][i] = max(dp[0][i - 1], dp[2][i - 1]) + arr[1][i]

        dp[2][i] = max(dp[0][i - 1], dp[1][i - 1], dp[2][i - 1])
    
    answer = max(dp[0][n - 1], dp[1][n - 1], dp[2][n - 1])

    print(answer)
