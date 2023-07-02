# A와 B, 12904번, 백준

# my thoughts :
# 1. S -> T로 가는 방식 대신 거꾸로 T -> S로 가는 방식으로 문제에 접근한다.

import sys

S = sys.stdin.readline().rstrip()
T = sys.stdin.readline().rstrip()

while len(T) > len(S):
    if T[-1] == "A":
        T = T[0:len(T) - 1:1]
    else:
        T = T[0:len(T) - 1:1][-1::-1]

if T == S:
    print(1)
else:
    print(0)
