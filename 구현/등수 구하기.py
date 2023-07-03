# 등수 구하기, 1205번, 백준

# my thoughts :
# 1. 일단 태수의 새 점수가 랭킹 리스트에 올라갈 수 있는지 여부를 먼저 구합니다.
# 2. 만약 태수의 새 점수가 랭킹 리스트에 올라갈 수 없다면 -1을 출력하고 종료합니다.
# 3. 만약 태수의 새 점수가 랭킹 리스트에 올라갈 수 있다면 ....

import sys

n, taesu, p = map(int, sys.stdin.readline().rstrip().split())

if n != 0:
    score = list(map(int, sys.stdin.readline().rstrip().split()))
else:
    score = list()

checkFlag = False # <<-- "태수의 새 점수가 랭킹 리스트에 올라갈 수 있는지에 대한 여부를 체킹하는 변수의 선언입니다..!!"

if n < p:
    checkFlag = True

    if not score:
        score.append(taesu)
    elif taesu <= score[-1]:
        score.append(taesu)
    else:
        for i in range(0, len(score), 1):
            if taesu > score[i]:
                score.insert(i, taesu)
                break
elif n == p:
    for i in range(0, len(score), 1):
        if taesu > score[i]:
            checkFlag = True
            score.insert(i, taesu)
            score = score[0:p:1]
            break

if checkFlag == False:
    print(-1)
else:
    for i in range(0, len(score), 1):
        if score[i] == taesu:
            print(i + 1)
            break
