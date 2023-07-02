# 세탁소 사장 동혁, 2720번, 백준

# my thoughts :
# 1. By using Greedy Algorithm, We can solve it..!!

import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    c = int(sys.stdin.readline().rstrip())

    answer = [0, 0, 0, 0]

    q, r = divmod(c, 25)
    answer[0] = q
    c = r

    q, r = divmod(c, 10)
    answer[1] = q
    c = r

    q, r = divmod(c, 5)
    answer[2] = q
    c = r

    q, r = divmod(c, 1)
    answer[3] = q
    c = r

    for val in answer:
        print(val, end = " ")
    print()
