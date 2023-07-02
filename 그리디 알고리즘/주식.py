# 주식, 11501번, 백준

import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    answer = 0

    n = int(sys.stdin.readline().rstrip())

    arr = list(map(int, sys.stdin.readline().rstrip().split()))

    max_val = arr[-1]
    cur_benefit = 0


    for i in range(len(arr) - 2, -1, -1):
        if arr[i] < max_val:
            cur_benefit += max_val - arr[i]
        elif arr[i] == max_val:
            pass
        elif arr[i] > max_val:
            answer += cur_benefit
            cur_benefit = 0
            max_val = arr[i]
    
    answer += cur_benefit
    
    print(answer)
