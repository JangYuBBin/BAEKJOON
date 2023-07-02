# 등수 매기기, 2012번, 백준
 
# my thoughts :
# 1. By using Sorting, We can solve it..!!

import sys

n = int(sys.stdin.readline().rstrip())

arr = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
arr.sort()

check = list(range(1, n + 1, 1))

answer = 0

for i in range(0, n, 1):
    answer += abs(arr[i] - check[i])

print(answer)
