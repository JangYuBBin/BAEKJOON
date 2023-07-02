# 게임을 만든 동준이, 2847번, 백준

# my thoughts :
# 1. By using Greedy Algorithm, We can solve it..!!

import sys

answer = 0

n = int(sys.stdin.readline().rstrip())

arr = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

arr = arr[-1::-1]

for i in range(0, n - 1, 1):
    if arr[i] > arr[i + 1]:
        pass
    elif arr[i] <= arr[i + 1]:
        answer += arr[i + 1] - arr[i] + 1

        arr[i + 1] = arr[i] - 1

print(answer)
