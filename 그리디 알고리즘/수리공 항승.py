# 수리공 항승, 1449번, 백준

# my thoughts :
# 1. By using Greedy Algorithm, We can solve it..!!

import sys

n, l = map(int, sys.stdin.readline().rstrip().split())

arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()

answer = 0

cover = 0

for val in arr:
    if cover >= val:
        pass
    elif cover < val:
        answer += 1

        cover = val + l - 1

print(answer)
