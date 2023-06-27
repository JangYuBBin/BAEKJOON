# 내리막길, 1520번, 백준

# my thoughts :
# 1. 그냥 단순하게 DFS를 활용한다면 시간초과를 받을 것입니다..!!
# 2. 그래서 우리는 Dynamic Programming을 활용해야 합니다..!!
# 3. dp[x][y] : (x, y)에서 (n - 1, m - 1)까지 내리막길로만 이동하는 경로의 갯수
# 4. 결국 우리가 구해야 하는 것은 dp[0][0]입니다..!!

import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

board = list()
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

dp = [[-1] * m for _ in range(n)]
dp[n - 1][m - 1] = 1
# 참고 > dp[x][y] = -1 : (x, y)에서 (n - 1, m - 1)까지 가는 경우의 수를 아직 구하지 못한 경우


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
            if board[new_v[0]][new_v[1]] < board[cur_v[0]][cur_v[1]]:
                dp[cur_v[0]][cur_v[1]] += dfs(new_v)
    
    return dp[cur_v[0]][cur_v[1]]

print(dfs((0, 0)))
