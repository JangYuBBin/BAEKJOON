# 기타줄, 1049번, 백준

# my thoughts :
# 1. q, r = divmod(N, 6)
# 2. q * 6개의 기타줄을 먼저 처리한 후 
# 3. r개의 기타줄을 처리..!!

import sys

answer = 0

n, m = map(int, sys.stdin.readline().rstrip().split())

arr = list()
for _ in range(m):
    val1, val2 = map(int, sys.stdin.readline().rstrip().split())

    arr.append((val1, val2))

q, r = divmod(n, 6)

# 일단, 먼저 q * 6개의 기타줄을 먼저 처리합시다..!!
min_cost = float("inf")

for i in range(0, m, 1):
    if min_cost > arr[i][0] * q:
        min_cost = arr[i][0] * q
    
    if min_cost > arr[i][1] * q * 6:
        min_cost = arr[i][1] * q * 6

answer += min_cost

# 그런다음, r개의 기타줄을 처리합시다..!!
min_cost = float("inf")

for i in range(0, m, 1):
    if min_cost > arr[i][0]:
        min_cost = arr[i][0]
    
    if min_cost > arr[i][1] * r:
        min_cost = arr[i][1] * r

answer += min_cost

print(answer)
