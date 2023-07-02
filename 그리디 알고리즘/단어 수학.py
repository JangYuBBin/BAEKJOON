# 단어 수학, 1339번, 백준

# my thoughts :
# 1. 각 알파벳마다의 비중을 계산해서 비중이 높은 알파벳부터 숫자 9부터 숫자 0까지 차례대로 부여합시다..!!
# 2. 중요한 문제이므로 나중에 다시 풀면 좋을 것 같습니다..!!

import sys
from collections import defaultdict

n = int(sys.stdin.readline().rstrip())

d = defaultdict(int) # <<-- "각 알파벳마다의 비중을 계산할 딕셔너리 자료형의 선언입니다..!!"

for _ in range(n):
    str = sys.stdin.readline().rstrip()

    for i in range(0, len(str), 1):
        d[str[i]] += 10**(len(str) - i - 1)

arr = list()

for k, v in d.items():
    arr.append((k, v))

arr.sort(key = lambda x : x[1], reverse = True)

answer = 0

for num, (k, v) in zip(list(range(9, -1, -1))[0:len(arr):1], arr):
    answer += num * v

print(answer)
