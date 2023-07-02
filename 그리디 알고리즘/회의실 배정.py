# 회의실 배정, 1931번, 백준

# my thoughts :
# 1. By using Greedy Algorithm, We can solve it..!!
# 2. 참고로 그리디 알고리즘 문제를 푸는 데 있어서 정렬 기준은 매우 중요하다고 말할 수 있습니다..!!
# 3. 일단 n개의 회의를 끝나는 시각이 빠른 순으로 정렬합니다. 만약 끝나는 시각이 같다면 시작시각이 빠른 것을 기준으로 정렬을 해줍니다.
# 4. ....

import sys

n = int(sys.stdin.readline().rstrip())

arr = list()

for _ in range(n):
    start, end = map(int, sys.stdin.readline().rstrip().split())

    arr.append((start, end))

arr.sort(key = lambda x : (x[1], x[0]), reverse = False)

end_time = arr[0][1]
answer = 1

for i in range(1, n, 1):
    if end_time <= arr[i][0]:
        end_time = arr[i][1]

        answer += 1

print(answer)
