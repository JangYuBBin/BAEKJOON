# ZOAC 4, 23971번, 백준

import sys

h, w, n, m = map(int, sys.stdin.readline().rstrip().split())

garo = 0
for j in range(0, w, m + 1):
    garo += 1

sero = 0
for i in range(0, h, n + 1):
    sero += 1

answer = sero * garo

print(answer)
