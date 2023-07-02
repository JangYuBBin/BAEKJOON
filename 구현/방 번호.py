# 방 번호, 1475번, 백준

# my thoughts :
# 1. 6은 9를 뒤집어서 이용할 수 있고, 9는 6을 뒤집어서 이용할 수 있다는 점을 유의해야 합니다..!!

import sys

arr = list(map(int, list(sys.stdin.readline().rstrip())))

d = dict()
d[0] = 0
d[1] = 0
d[2] = 0
d[3] = 0
d[4] = 0
d[5] = 0
d[6] = 0
d[7] = 0
d[8] = 0

for num in arr:
    if num == 9:
        d[6] += 1
    else:
        d[num] += 1

if d[6] % 2 == 1:
    d[6] = d[6] // 2 + 1
else:
    d[6] = d[6] // 2

answer = 0

for k in d.keys():
    if answer < d[k]:
        answer = d[k]

print(answer)
