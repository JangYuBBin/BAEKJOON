# 수들의 합, 1789번, 백준

# my thoughts :
# 1. 최대한 작은 수들 여러 개로 S를 만들어야 합니다.
# 2. 따라서 1부터 차례대로 더할려고 노력해서 S를 만들어야 합니다.
# 3. n = 1, 2, 3, .... 순으로 확인하면서 1 ~ n까지의 합이 S를 넘기게 되는 n이 있을 때 n - 1이 자연수 N의 최댓값이 되는 것입니다.

import sys

s = int(sys.stdin.readline().rstrip())

n = 1

while True:
    sum = n * (n + 1) // 2

    if sum > s:
        print(n - 1)
        break
    elif sum <= s:
        n += 1
