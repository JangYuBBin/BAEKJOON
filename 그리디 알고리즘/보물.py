# 보물, 1026번, 백준

# my thoughts :
# 1. 결국 S의 값을 가장 작게 만들기 위해서는 A를 내림차순 정렬하고 B를 오름차순 정렬을 한 다음 A[i] x B[i]의 합을 구해주면 될 것입니다..!!

import sys

n = int(sys.stdin.readline().rstrip())

A = list(map(int, sys.stdin.readline().rstrip().split()))
B = list(map(int, sys.stdin.readline().rstrip().split()))

A.sort(reverse = True)
B.sort(reverse = False)

answer = 0

for i in range(0, n, 1):
    answer += A[i] * B[i]

print(answer)
