# 벌집, 2292번, 백준

import sys

n = int(sys.stdin.readline().rstrip())

if n == 1:
    print(1)
elif 2 <= n <= 7:
    print(2)
else:
    start = 2
    end = 7

    for i in range(1, 1_000_000_000, 1):
        start += 6 * i
        end += 6 * (i + 1)

        if start <= n <= end:
            print(i + 2)
            break
