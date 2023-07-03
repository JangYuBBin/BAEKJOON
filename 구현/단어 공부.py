# 단어 공부, 1157번, 백준

import sys
from collections import defaultdict

str = sys.stdin.readline().rstrip()

str = str.lower()

d = defaultdict(int)

for c in str:
    d[c] += 1

arr = list()

for k, v in d.items():
    arr.append((k, v))

arr.sort(key = lambda x : x[1], reverse = True)

for i in range(1, len(arr), 1):
    if arr[i][1] == arr[0][1]: # <<-- " 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다."
        print("?")
        exit()
    else:
        break

print(arr[0][0].upper())
