# 행렬, 1080번, 백준

# my thoughts :
# 1. By using Greedy Algorithm, We can solve it..!!

import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

A = list()
for _ in range(n):
    A.append(list(map(int, list(sys.stdin.readline().rstrip()))))

B = list()
for _ in range(n):
    B.append(list(map(int, list(sys.stdin.readline().rstrip()))))

if n < 3 or m < 3: # <<-- "3 x 3 크기의 부분 행렬에 있는 모든 원소를 뒤집는 행위를 할 수 없는 상황이라면..!!"
    for i in range(0, n, 1):
        for j in range(0, m, 1):
            if A[i][j] != B[i][j]:
                print(-1)
                exit()
            else:
                pass
    print(0)
    exit()

answer = 0

for i in range(0, n - 2, 1):
    for j in range(0, m - 2, 1):
        if A[i][j] != B[i][j]:
            answer += 1

            for k in range(i, i + 3, 1):
                for l in range(j, j + 3, 1):
                    if A[k][l] == 1:
                        A[k][l] = 0
                    else:
                        A[k][l] = 1
        else:
            pass

for i in range(0, n, 1):
    for j in range(0, m, 1):
        if A[i][j] != B[i][j]:
            print(-1)
            exit()
        else:
            pass

print(answer)
