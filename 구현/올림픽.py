# 올림픽, 8979번, 백준

import sys
from collections import defaultdict

n, k = map(int, sys.stdin.readline().rstrip().split())

scores = defaultdict(list)

for _ in range(n):
    score = list(map(int, sys.stdin.readline().rstrip().split()))
    nara = score.pop(0)

    scores[nara] = score

answer = 1

for i in range(1, n + 1, 1):
    if i == k:
        continue
    else:
        if scores[i][0] > scores[k][0]:
            answer += 1
        elif scores[i][0] == scores[k][0] and scores[i][1] > scores[k][1]:
            answer += 1
        elif scores[i][0] == scores[k][0] and scores[i][1] == scores[k][1] and scores[i][2] > scores[k][2]:
            answer += 1

print(answer)
