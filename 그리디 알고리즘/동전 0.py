# 동전 0, 11047번, 백준

# my thoughts :
# 1. By using Greedy Algorithm, We can solve it..!!

import sys

answer = 0

n, k = map(int, sys.stdin.readline().rstrip().split())

arr = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
arr = arr[-1::-1]

for i in range(0, n, 1):
    q, r = divmod(k, arr[i])

    answer += q

    k = r

print(answer)
