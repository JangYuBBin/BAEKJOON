# 퇴사, 14501번, 백준

# my thoughts :
# 1. Dynamic Programming 태그에 있는 문제였지만 저는 BFS를 활용하여 이 문제를 풀어보았습니다.
# 2. 다음에 다시 풀어보면 좋을 문제인 것 같습니다..!!

import sys
from collections import deque

answer = list()

n = int(sys.stdin.readline().rstrip())

arr = [(0, 0)]

for _ in range(n):
    t, p = map(int, sys.stdin.readline().rstrip().split())

    arr.append((t, p))

for start_day in range(1, n + 1, 1):
    end_day = start_day + arr[start_day][0] - 1
    
    if end_day <= n:
        queue = deque()

        queue.append((end_day, arr[start_day][1]))

        while queue:
            end_day, cur_value = queue.popleft()

            checkFlag = False

            for i in range(end_day + 1, n + 1, 1):
                new_end_day = i + arr[i][0] - 1

                if new_end_day <= n:
                    queue.append((new_end_day, cur_value + arr[i][1]))

                    checkFlag = True
            
            if checkFlag == False:
                answer.append(cur_value)

if answer:
    print(max(answer))
else:
    print(0)
