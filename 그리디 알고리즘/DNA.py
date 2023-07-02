# DNA, 1969번, 백준

# my thoughts :
# 1. 문제 이해를 잘 해야할 것 같습니다..!!

import sys
from collections import defaultdict

n, m = map(int, sys.stdin.readline().rstrip().split())

dnas = [sys.stdin.readline().rstrip() for _ in range(n)]

answer = ""

for i in range(0, m, 1):
    d = defaultdict(int)

    for j in range(0, n, 1):
        d[dnas[j][i]] += 1
    
    arr = list()

    for k, v in d.items():
        arr.append((k, v))
    
    arr.sort(key = lambda x : (-x[1], x[0]), reverse = False)

    answer += arr[0][0]

cnt = 0

for i in range(0, n, 1):
    for j in range(0, m, 1):
        if answer[j] != dnas[i][j]:
            cnt += 1

print(answer)
print(cnt)
