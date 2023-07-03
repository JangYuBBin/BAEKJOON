# 삼각형과 세 변, 5073번, 백준

import sys

while True:
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    if a == b == c == 0:
        break
    else:
        pass

    arr = [a, b, c]
    arr.sort()

    if arr[2] >= arr[0] + arr[1]:
        print("Invalid")
    elif arr[0] == arr[1] == arr[2]:
        print("Equilateral")
    elif arr[0] == arr[1] or arr[1] == arr[2] or arr[0] == arr[2]:
        print("Isosceles")
    else:
        print("Scalene")
