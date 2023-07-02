# 요세푸스 문제 0, 11866번, 백준

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
