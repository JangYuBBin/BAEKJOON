# 피보나치 함수, 1003번, 백준

# my thoughts :
# 1. By using Dynamic Programming, We can solve it..!!
# 2. dp_1[i] : f(i)에서 f(1)이 호출되는 횟수
# 3. dp_0[i] : f(i)에서 f(0)이 호출되는 횟수

import sys

dp_0 = [0] * (40 + 1)
dp_0[0] = 1
dp_0[1] = 0

for i in range(2, 40 + 1, 1):
    dp_0[i] = dp_0[i - 1] + dp_0[i - 2]

dp_1 = [0] * (40 + 1)
dp_1[0] = 0
dp_1[1] = 1

for i in range(2, 40 + 1, 1):
    dp_1[i] = dp_1[i - 1] + dp_1[i - 2]

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())

    print(dp_0[n], end = " ")
    print(dp_1[n])
