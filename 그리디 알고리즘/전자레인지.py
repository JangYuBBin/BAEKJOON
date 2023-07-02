# 전자레인지, 10162번, 백준

# my thoughts :
# 1. By using Greedy Algorithm, We can solve it..!!

import sys

t = int(sys.stdin.readline().rstrip())

answer = [0, 0, 0]

q, r = divmod(t, 300)
answer[0] += q
t = r

q, r = divmod(t, 60)
answer[1] += q
t = r

q, r = divmod(t, 10)
answer[2] += q
t = r

if t != 0:
    print(-1)
else:
    print(answer[0], answer[1], answer[2])
