# 배, 1092번, 백준

# my thoughts :
# 1. 문제를 푸는 로직은 떠올리기 쉬우나 구현이 어려웠던 문제인 것 같습니다.
# 2. 틀린 문제이므로 나중에 다시 풀어보아야 할 것 같습니다..!!

import sys

n = int(sys.stdin.readline().rstrip())
cranes = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
boxes = list(map(int, sys.stdin.readline().rstrip().split()))

cranes.sort(reverse = True)
boxes.sort(reverse = True)

if boxes[0] > cranes[0]:
    print(-1)
    exit()

answer = 0

while boxes:
    for crane in cranes:
        for box in boxes:
            if crane >= box:
                boxes.remove(box)
                break
    
    answer += 1

print(answer)
