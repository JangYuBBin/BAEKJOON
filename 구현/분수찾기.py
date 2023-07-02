# 분수찾기, 1193번, 백준

# my thoughts :
# 1. 일단 X번째 분수가 몇 번째 줄에 있는지 확인한다.
# 2. 몇 번째 줄에 있는지 확인했다면 그 다음으로 해당 줄에서 몇 번째로 존재하는지 확인하면 됩니다..!!

import sys

x = int(sys.stdin.readline().rstrip())

if x == 1:
    print("1/1")
    exit()

for i in range(1, 10_000_000, 1):
    if (i - 1) * i // 2 < x <= i * (i + 1) // 2:
        q = i # 몇번째 줄인가?
        r = x - (i - 1) * i // 2 # 해당 줄에서 몇번째 순서인가?
        break

if q % 2 == 0: # <<-- "짝수 번째 줄이라면 위에서 아래로 진행..!!"
    bunmo, bunza = r, (q + 1) - r
else: # <<-- "홀수 번째 줄이라면 아래에서 위로 진행..!!"
    bunmo, bunza = (q + 1) - r, r

print(bunmo, end = "")
print("/", end = "")
print(bunza)
