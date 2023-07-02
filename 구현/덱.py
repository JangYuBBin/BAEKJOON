# 덱, 10866번, 백준

import sys
from collections import deque

deque = deque()

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    order = sys.stdin.readline().rstrip().split()

    if order[0] == "push_front":
        deque.appendleft(int(order[1]))
    elif order[0] == "push_back":
        deque.append(int(order[1]))
    elif order[0] == "pop_front":
        if not deque:
            print(-1)
        else:
            print(deque.popleft())
    elif order[0] == "pop_back":
        if not deque:
            print(-1)
        else:
            print(deque.pop())
    elif order[0] == "size":
        print(len(deque))
    elif order[0] == "empty":
        if not deque:
            print(1)
        else:
            print(0)
    elif order[0] == "front":
        if not deque:
            print(-1)
        else:
            print(deque[0])
    elif order[0] == "back":
        if not deque:
            print(-1)
        else:
            print(deque[-1])
