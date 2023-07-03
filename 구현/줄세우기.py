# 줄세우기, 10431번, 백준

import sys

p = int(sys.stdin.readline().rstrip())

for _ in range(p):
    orders = list(map(int, sys.stdin.readline().rstrip().split()))
    t = orders.pop(0)

    arr = list()

    answer = 0 # <<-- "학생들이 공간을 마련하기 위해 한 발씩 뒤로 물러나는 행위의 횟수입니다..!!"

    for order in orders:
        if not arr:
            arr.append(order)
        elif arr:
            checkFlag = False
            idx = -1

            for i in range(0, len(arr), 1):
                if arr[i] > order:
                    checkFlag = True
                    idx = i
                    break
            
            if checkFlag == False:
                arr.append(order)
            elif checkFlag == True:
                answer += (len(arr) - idx) * 1
                arr.insert(idx, order)
    
    print(t, end = " ")
    print(answer)

