# 비밀번호 발음하기, 4659번, 백준

import sys

moeum = ["a", "e", "i", "o", "u"]

while True:
    password = sys.stdin.readline().rstrip()
    if password == "end":
        break
    else:
        pass

    checkFlag = False # <<-- "비밀번호가 높은 품질의 조건을 가진 비밀번호인가..??"

    # 1. 모음(a, e, i, o, u) 하나를 반드시 포함해야 한다.
    for c in password:
        if c in moeum:
            checkFlag = True
            break
    
    if checkFlag == True:
        pass
    else:
        print("<" + password + ">", end = " ")
        print("is not acceptable.")
        continue

    # 2. 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
    for i in range(0, len(password) - 2, 1):
        if password[i] in moeum and password[i + 1] in moeum and password[i + 2] in moeum:
            checkFlag = False
            break
        elif password[i] not in moeum and password[i + 1] not in moeum and password[i + 2] not in moeum:
            checkFlag = False
            break
    
    if checkFlag == True:
        pass
    else:
        print("<" + password + ">", end = " ")
        print("is not acceptable.")
        continue

    # 3. 같은 글자가 연속적으로 두번 오면 안되나, ee와 oo는 허용한다.
    for i in range(0, len(password) - 1, 1):
        if password[i] == password[i + 1]:
            if password[i] == password[i + 1] == "e":
                continue
            elif password[i] == password[i + 1] == "o":
                continue
            else:
                checkFlag = False
                break
    
    if checkFlag == True:
        print("<" + password + ">", end = " ")
        print("is acceptable.")
    else:
        print("<" + password + ">", end = " ")
        print("is not acceptable.")
