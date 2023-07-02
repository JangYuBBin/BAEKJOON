# 그룹 단어 체커, 1316번, 백준

import sys
from collections import defaultdict

n = int(sys.stdin.readline().rstrip())

answer = 0

for _ in range(n):
    str = sys.stdin.readline().rstrip()

    stack = list()

    for c in str:
        if not stack:
            stack.append(c)
        elif stack:
            if stack[-1] == c:
                pass
            else:
                stack.append(c)
    
    d = defaultdict(int)

    for c in stack:
        d[c] += 1
    
    checkFlag = True

    for k in d.keys():
        if d[k] >= 2:
            checkFlag = False
            break
    
    if checkFlag == True:
        answer += 1
    else:
        pass

print(answer)
