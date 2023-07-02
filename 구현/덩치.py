# 덩치, 7568번, 백준

import sys

n = int(sys.stdin.readline().rstrip())

arr = list()

for _ in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())

    arr.append((x, y))

answer = list()

for i in range(0, n, 1):
    cnt = 0

    for j in range(0, n, 1):
        if j == i:
            continue
        else:
            if arr[j][0] > arr[i][0] and arr[j][1] > arr[i][1]:
                cnt += 1
    
    answer.append(cnt + 1)

for val in answer:
    print(val, end = " ")
