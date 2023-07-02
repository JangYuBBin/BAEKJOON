# 통계학, 2108번, 백준

import sys
from collections import defaultdict

n = int(sys.stdin.readline().rstrip())

arr = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

# 산술평균
answer1 = round(sum(arr) / n)

# 중앙값
arr.sort()

answer2 = arr[(n - 1) // 2]

# 최빈값
d = defaultdict(int)

for val in arr:
    d[val] += 1

temp = list()

for k, v in d.items():
    temp.append((k, v))

temp.sort(key = lambda x : (x[1], -x[0]), reverse = True)

check = list()

for k, v in temp:
    if temp[0][1] == v:
        check.append(k)

check.sort()

if len(check) == 1:
    answer3 = check[0]
else:
    answer3 = check[1]

# 범위
answer4 = arr[-1] - arr[0]

print(answer1)
print(answer2)
print(answer3)
print(answer4)
