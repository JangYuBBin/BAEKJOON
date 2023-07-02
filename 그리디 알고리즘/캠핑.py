# 캠핑, 4796번, 백준

# my thoughts :
# 1. divmod()를 활용하여 문제를 해결해봅시다..!!
# 2. 그리디 알고리즘은 약간의 감도 필요합니다..!!

import sys

cnt = 1
while True:
    l, p, v = map(int, sys.stdin.readline().rstrip().split())
    if l == p == v == 0:
        break

    q, r = divmod(v, p)

    answer = 0
    answer += q * l
    answer += min(r, l)

    print("Case %d: " %cnt, end = "")
    cnt += 1
    print(answer)
