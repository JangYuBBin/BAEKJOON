# 거스름돈, 5585번, 백준

# my thoughts :
# 1. By using Greedy Algoritm, We can solve it..!!

import sys

m = 1000 - int(sys.stdin.readline().rstrip())

answer = 0

q, r = divmod(m, 500)
answer += q
m = r

q, r = divmod(m, 100)
answer += q
m = r

q, r = divmod(m, 50)
answer += q
m = r

q, r = divmod(m, 10)
answer += q
m = r

q, r = divmod(m, 5)
answer += q
m = r

q, r = divmod(m, 1)
answer += q
m = r

print(answer)
