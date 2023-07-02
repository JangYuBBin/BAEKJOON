# 스택, 10828번, 백준

import sys

n = int(sys.stdin.readline().rstrip())

stack = []

for _ in range(n):
    order = sys.stdin.readline().rstrip().split()

    if order[0] == "push":
        stack.append(int(order[1]))
    elif order[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif order[0] == "size":
        print(len(stack))
    elif order[0] == "empty":
        if not stack:
            print(1)
        else:
            print(0)
    elif order[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
