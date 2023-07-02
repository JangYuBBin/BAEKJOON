# A -> B, 16953번, 백준

# my thoughts :
# 1. By using Greedy Algorithm, We can solve it..!!
# 2. A -> B로 가는 방식이 아닌 거꾸로 B -> A로 가는 방식으로 접근해봅시다..!!
# 3. 내일 다시 풀어보도록 합시다..!!

import sys

A, B = map(int, sys.stdin.readline().rstrip().split())

answer = 0

while B != A:
    if B < A:
        print(-1)
        exit()
    else:
        pass

    if B % 2 == 0:
        B //= 2

        answer += 1
    elif str(B)[-1] == "1":
        B = int(str(B)[0:len(str(B)) - 1:1])

        answer += 1
    else:
        print(-1)
        exit()

print(answer + 1)
