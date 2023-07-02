# 제로, 10773번, 백준

# my thoughts :
# 1. By using Stack, We can solve it..!!

import sys

k = int(sys.stdin.readline().rstrip())

stack = list()

for _ in range(k):
    num = int(sys.stdin.readline().rstrip())

    if num == 0:
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))
