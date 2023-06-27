# 행렬 곱셈 순서, 11049번, 백준

# my thoughts :
# 1. 어렵고 틀린 문제이므로 나중에 다시 풀어보아야 할 것 같습니다..!!
# 2. By using Dynamic Programming, We can solve it..!!
# 3. dp[i][j] : i번째 행렬부터 j번째 행렬까지 곱하는데 필요한 곱셈 연산의 수의 최솟값
# 4. 길이가 1인 행렬은 곱할 수 없으므로 연산의 수는 0이 된다.
# 5. 길이가 2인 행렬은 그냥 곱하는 것이 답이다.
# 6. ....

import sys

n = int(sys.stdin.readline().rstrip())

arr = list()

for _ in range(n):
    r, c = map(int, sys.stdin.readline().rstrip().split())

    arr.append((r, c))

dp = [[float("inf")] * n for _ in range(n)]

for l in range(1, n + 1, 1):
    for start in range(0, n - l + 1, 1):
        end = start + l - 1

        if l == 1:
            dp[start][end] = 0
        elif l == 2:
            dp[start][end] = arr[start][0] * arr[start][1] * arr[end][1]
        else:
            for mid in range(start, end, 1):
                dp[start][end] = min(dp[start][end], dp[start][mid] + dp[mid + 1][end] + arr[start][0] * arr[mid][1] * arr[end][1])

print(dp[0][n - 1])
