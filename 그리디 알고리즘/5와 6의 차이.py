# 5와 6의 차이, 2864번, 백준

import sys

a, b = sys.stdin.readline().rstrip().split()

min_a = a.replace("6", "5")
min_b = b.replace("6", "5")

min_answer = int(min_a) + int(min_b)

max_a = a.replace("5", "6")
max_b = b.replace("5", "6")

max_answer = int(max_a) + int(max_b)

print(min_answer, end = " ")
print(max_answer)
