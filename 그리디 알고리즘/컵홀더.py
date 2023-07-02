# 컵홀더, 2810번, 백준

import sys

n = int(sys.stdin.readline().rstrip())

str = sys.stdin.readline().rstrip()

str = str.replace("S", "*S*").replace("LL", "*LL*").replace("**", "*")

# print(str)
# 출력결과 Ex : *S*LL*LL*S*S*LL*

str = str.replace("*S", "").replace("*L", "").replace("S*", "").replace("L*", "")

answer = n

for c in str:
    if c == "L" or c == "S":
        answer -= 1

print(answer)
