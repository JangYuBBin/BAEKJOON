# 저울, 2437번, 백준

# my thoughts :
# 1. By using Greedy Algorithm, We can solve it..!!

import sys

n = int(sys.stdin.readline().rstrip())

arr = list(map(int, sys.stdin.readline().rstrip().split()))

arr.sort()

cur_max = 0

for val in arr:
    if cur_max + 1 >= val:
        cur_max += val
    else:
        print(cur_max + 1)
        exit()

print(cur_max + 1)
