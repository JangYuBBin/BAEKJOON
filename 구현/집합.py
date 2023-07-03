# 집합, 11723번, 백준

import sys

S = set()

m = int(sys.stdin.readline().rstrip())

for _ in range(m):
    order = sys.stdin.readline().rstrip().split()

    if order[0] == "add":
        S.add(order[1])
    elif order[0] == "remove":
        if order[1] in S:
            S.remove(order[1])
        else:
            pass
    elif order[0] == "check":
        if order[1] in S:
            print(1)
        else:
            print(0)
    elif order[0] == "toggle":
        if order[1] in S:
            S.remove(order[1])
        else:
            S.add(order[1])
    elif order[0] == "all":
        S = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",}
    elif order[0] == "empty":
        S = set()
