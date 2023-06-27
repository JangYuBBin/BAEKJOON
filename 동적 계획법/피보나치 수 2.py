# 피보나치 수 2, 2748번, 백준

# my thoughts :
# 1. By using Dynamic Programming, We can solve it..!!

import sys

n = int(sys.stdin.readline().rstrip())

f = [0] * (n + 1)
f[0] = 0
f[1] = 1

if n == 1:
    print(f[1])
    exit()
else:
    pass

for i in range(2, n + 1, 1):
    f[i] = f[i - 1] + f[i - 2]

print(f[n])
