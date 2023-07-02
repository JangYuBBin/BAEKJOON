# 로프, 2217번, 백준

# my thoughts :
# 1. n개의 로프를 버틸 수 있는 최대 중량을 기준으로 오름차순 정렬한다.
# 2. 정렬된 배열을 순회하면서 이 로프들을 이용하여 들어올릴 수 있는 물체의 최대 중량을 구해낸다..!!
# 3. 그리디 알고리즘 관련 문제를 풀 때에는 약간의 센스가 필요한 것 같습니다..!!

import sys

n = int(sys.stdin.readline().rstrip())

arr = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

arr.sort()

answer = 0 

for i in range(0, n, 1):
    val = arr[i] * (n - i)

    if answer < val:
        answer = val

print(answer)
