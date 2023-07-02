# 크게 만들기, 2812번, 백준

# my thoughts :
# 1. By using Greedy Algorithm, We can solve it..!!
# 2. stack을 활용한다.
# 3. .... ..!!

import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

nums = list(map(int, list(sys.stdin.readline().rstrip())))

stack = []

for num in nums:
    if not stack:
        stack.append(num)
    elif stack:
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        
        stack.append(num)

while k > 0:
    stack.pop()
    k -= 1

answer = "".join(list(map(str, stack)))

print(answer)
