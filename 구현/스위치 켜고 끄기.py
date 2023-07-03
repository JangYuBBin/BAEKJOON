# 스위치 켜고 끄기, 1244번, 백준

import sys

n = int(sys.stdin.readline().rstrip()) # 스위치의 개수

arr = list(map(int, sys.stdin.readline().rstrip().split())) # 스위치의 상태

t = int(sys.stdin.readline().rstrip()) # 학생수

for _ in range(t):
    gender, location = map(int, sys.stdin.readline().rstrip().split())

    if gender == 1: # 남성이면
        for i in range(location, n + 1, location):
            i -= 1

            if arr[i]:
                arr[i] = 0
            else:
                arr[i] = 1
    else: # 여성이면
        start = location - 1
        diff = 0

        for i in range(1, n, 1):
            if start - i < 0 or start + i >= n:
                break
            elif arr[start - i] == arr[start + i]:
                diff = i
            elif arr[start - i] != arr[start + i]:
                break
        
        for i in range(start - diff, start + diff + 1, 1):
            if arr[i]:
                arr[i] = 0
            else:
                arr[i] = 1

for i in range(0, n, 1):
    print(arr[i], end=" ")

    if (i + 1) % 20 == 0 or i == n - 1:
        print()
