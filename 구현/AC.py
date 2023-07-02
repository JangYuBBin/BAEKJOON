# AC, 5430번, 백준

# my thoughts :
# 1. R(뒤집기) 함수를 어떻게 처리하느냐에 따라서 시간초과를 피하느냐 마느냐..!!

import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    p = sys.stdin.readline().rstrip()

    n = int(sys.stdin.readline().rstrip())

    arr = sys.stdin.readline().rstrip()

    if n == 0:
        queue = deque()
    else:
        arr = arr[1:len(arr)-1:1]
        arr = arr.split(",")
        queue = deque(arr)

    direction = "left"
    
    checkFlag = True
    for c in p:
        if c == "R":
            if direction == "left":
                direction = "right"
            elif direction == "right":
                direction = "left"
        elif c == "D":
            if not queue:
                checkFlag = False
                break
            elif queue:
                if direction == "left":
                    queue.popleft()
                elif direction == "right":
                    queue.pop()
    
    if checkFlag == True:
        if direction == "left":
            print("[" + ",".join(queue) + "]")
        elif direction == "right":
            queue.reverse()
            print("[" + ",".join(queue) + "]")
    else:
        print("error")
