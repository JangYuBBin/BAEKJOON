# 임스와 함께하는 미니게임, 25757번, 백준

import sys

n, game = sys.stdin.readline().rstrip().split()
n = int(n)

already = set() # <<-- "임스와 같이 플레이한 사람의 이름을 저장할 집합 자료형의 선언입니다..!!"

waiting = set() # <<-- "일종의 대기방이라고 보시면 됩니다..!!"

check = 0 # <<-- "해당 게임에는 몇명의 인원이 필요한지..??"
if game == "Y":
    check = 1
elif game == "F":
    check = 2
elif game == "O":
    check = 3

answer = 0

for _ in range(n):
    name = sys.stdin.readline().rstrip()

    if name in already:
        continue
    else:
        if len(waiting) < check:
            waiting.add(name)
    
    if len(waiting) == check:
        answer += 1

        for w in waiting:
            already.add(w)
        
        waiting = set()

print(answer)
