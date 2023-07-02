# 뒤집기, 1439번, 백준

# my thoughts :
# 1. 0으로만 이루어진 부분의 갯수 1로만 이루어진 부분의 갯수를 구한다.
# 2. 만약 0으로 이루어진 부분의 갯수가 4개이고 1로만 이루어진 부분의 갯수가 3개이면 정답은 3이 될 것이다.
# 3. 즉, 0으로 이루어진 부분의 갯수와 1로 이루어진 부분의 갯수의 최솟값이 답이 되는 것입니다..!!

import sys

s = sys.stdin.readline().rstrip()

cnt_0 = 0
cnt_1 = 0

cur_str = ""

for i in range(0, len(s), 1):
    if i < len(s) - 1 and s[i] == "0" and s[i + 1] == "1":
        cnt_0 += 1
        cur_str = ""
    elif i < len(s) - 1 and s[i] == "1" and s[i + 1] == "0":
        cnt_1 += 1
        cur_str = ""
    else:
        cur_str += s[i]
if cur_str == "0" * len(cur_str):
    cnt_0 += 1
elif cur_str == "1" * len(cur_str):
    cnt_1 += 1

answer = min(cnt_0, cnt_1)

print(answer)
