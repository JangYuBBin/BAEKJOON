# 파일 합치기, 11066번, 백준

# my thoughts :
# 1. By using Dynamic Programming, We can solve it..!!
# 2. 인접한 두 파일만을 합칠 수 있다는 점을 유의해야 합니다.
# 3. dp[i][j] : i번째 인덱스부터 j번재 인덱스까지의 파일을 합칠 때 필요한 최소비용
# 4. 결국 우리가 구해야 하는 것은 dp[0][k - 1]입니다..!!
# 5. 어렵고 틀린 문제이므로 나중에 다시 풀어보아야 할 문제인 것 같습니다..!!

import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    k = int(sys.stdin.readline().rstrip())

    arr = list(map(int, sys.stdin.readline().rstrip().split()))

    S = [0] * k
    S[0] = arr[0]

    for i in range(1, k, 1):
        S[i] = S[i - 1] + arr[i]
    
    dp = [[float("inf")] * k for _ in range(k)]

    for l in range(1, k + 1, 1):
        for start in range(0, k - l + 1, 1):
            end = start + l - 1

            if l == 1: 
                dp[start][end] = 0 # <<-- "한 개의 파일은 합칠 수 없기 때문입니다..!!"
            elif l == 2:
                dp[start][end] = arr[start] + arr[end]
            else:
                for mid in range(start, end, 1):
                    if start == 0:
                        dp[start][end] = min(dp[start][end], dp[start][mid] + dp[mid + 1][end] + S[end])
                    else:
                        dp[start][end] = min(dp[start][end], dp[start][mid] + dp[mid + 1][end] + S[end] - S[start - 1])
                        
    print(dp[0][k - 1])
