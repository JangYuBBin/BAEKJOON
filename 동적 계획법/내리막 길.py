# 내리막길, 1520번, 백준

# my thoughts :
# 1. 어렵고 틀린 문제이므로 나중에 다시 풀어보아야 할 것 같습니다..!!
# 2. By using DFS and Dp, We can solve it..!!
# 3. dp[i][j] : (i, j)에서 (n - 1, m - 1)까지 내리막길로만 이동하는 경로의 갯수
# 4. 결국 우리가 구해야 하는 것은 dp[0][0]..!!

import sys
sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().rstrip().split())

arr = list()
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

dp = [[-1] * m for _ in range(n)]
dp[n - 1][m - 1] = 1

def dfs(cur_v):
    # Base Case
    if cur_v == (n - 1, m - 1):
        return dp[n - 1][m - 1]
    
    # Visited Case
    if dp[cur_v[0]][cur_v[1]] != -1:
        return dp[cur_v[0]][cur_v[1]]
    
    # Not Visited Case
    dp[cur_v[0]][cur_v[1]] = 0

    for d in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
        new_v = (cur_v[0] + d[0], cur_v[1] + d[1])

        if 0 <= new_v[0] < n and 0 <= new_v[1] < m:
            if arr[new_v[0]][new_v[1]] < arr[cur_v[0]][cur_v[1]]:
                dp[cur_v[0]][cur_v[1]] += dfs(new_v)
    
    return dp[cur_v[0]][cur_v[1]]

print(dfs((0, 0)))
