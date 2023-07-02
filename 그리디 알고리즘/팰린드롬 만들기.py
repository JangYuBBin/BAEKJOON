# 팰린드롬 만들기, 1213번, 백준

# my thoughts :
# 1. 팰린드롬을 만들기 위해서는 홀수개의 알파벳이 1개이하이어야 합니다.
# 2. 사전 순으로 가장 앞서는 팰린드롬을 만들기 위해서는 먼저 홀수개인 알파벳 1개를 먼저 붙입니다.
# 3. 그다음에는 Z -> A순으로 answer 문자열 앞뒤에 가지고 있는 갯수의 //2 만큼 앞뒤로 붙여줍니다..!!

import sys
from collections import defaultdict

str = sys.stdin.readline().rstrip()

d = defaultdict(int)

for c in str:
    d[c] += 1

check = 0

for k in d.keys():
    if d[k] % 2 == 1:
        check += 1

if check <= 1:
    pass
else:
    print("I'm Sorry Hansoo")
    exit()

answer = ""

for k in d.keys():
    if d[k] % 2 == 1:
        answer += k
        d[k] -= 1

arr = list()

for k in d.keys():
    arr.append((k, d[k]))

arr.sort(key = lambda x : x[0], reverse = True)

for k, v in arr:
    answer = k * (v // 2) + answer
    answer += k * (v // 2)

print(answer)
