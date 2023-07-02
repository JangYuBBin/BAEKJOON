# UCPC는 무엇의 약자일까?

# my thoughts :
# 1. By using Stack, We can solve it..!!

import sys

str = sys.stdin.readline().rstrip()

stack = ["C", "P", "C", "U"]

for c in str:
    if stack and c == stack[-1]:
        stack.pop()

if not stack:
    print("I love UCPC")
else:
    print("I hate UCPC")
