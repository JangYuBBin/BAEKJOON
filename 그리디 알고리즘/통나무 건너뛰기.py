# 통나무 건너뛰기

# my thoughts :
# 1. 문제 설명에 답이 있는 문제입니다..!!

import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())

    arr = list(map(int, sys.stdin.readline().rstrip().split()))

    arr.sort(reverse = False)

    answer = deque()

    answer.append(arr.pop())

    while arr:
        answer.append(arr.pop())

        if not arr:
            break

        answer.appendleft(arr.pop())
    
    max_diff = 0

    for i in range(0, len(answer), 1):
        if i == len(answer) - 1:
            if max_diff < abs(answer[i] - answer[0]):
                max_diff = abs(answer[i] - answer[0])
            continue
        
        if max_diff < abs(answer[i] - answer[i + 1]):
            max_diff = abs(answer[i] - answer[i + 1])
    
    print(max_diff)



