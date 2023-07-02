# 요세푸스 문제, 1158번, 백준

# my thoughts :
# 1. By using Deque Or Queue, We can solve it..!!

import sys
from collections import deque

n, k = map(int, sys.stdin.readline().rstrip().split())

queue = deque(list(range(1, n + 1, 1)))

answer = list()

while queue:
    for _ in range(k - 1):
        queue.append(queue.popleft())
    
    answer.append(queue.popleft())

print("<", end = "")
for i, val in enumerate(answer):
    if i == len(answer) - 1:
        print(val, end = ">")
    else:
        print(val, end = ", ")
