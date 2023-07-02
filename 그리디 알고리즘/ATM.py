# ATM, 11399번, 백준

# my thoughts :
# 1. By using Sorting, We can solve it..!!

import sys

n = int(sys.stdin.readline().rstrip())

arr = list(map(int, sys.stdin.readline().rstrip().split()))

arr.sort()

answer = 0

for i in range(0, n, 1):
    answer += sum(arr[0:i+1:1])

print(answer)
