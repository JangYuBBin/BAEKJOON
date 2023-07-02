# 프린터 큐, 1966번, 백준

import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().rstrip().split())

    arr = list(map(int, sys.stdin.readline().rstrip().split()))

    queue = deque()

    for i, val in enumerate(arr):
        queue.append((i, val))
    
    cnt = 0

    while queue:
        cur_idx, cur_val = queue.popleft()

        checkFlag = True

        for idx, val in queue:
            if cur_val < val:
                checkFlag = False
                break
        
        if checkFlag == True:
            cnt += 1

            if cur_idx == m:
                print(cnt)
                break
            else:
                pass
        else:
            queue.append((cur_idx, cur_val))
