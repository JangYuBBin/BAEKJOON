# 다리 놓기, 1010번, 백준

# my thoughts :
# 1. 결국 m개의 지점에서 n개의 지점을 선택하면 되는 문제이므로 조합과 관련된 문제라고 할 수 있습니다.
# 2. answer = mCn

import sys
from math import factorial

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().rstrip().split())

    answer = factorial(m) // factorial(n) // factorial(m - n)

    print(answer)
