# 잃어버린 괄호, 1541번, 백준

# my thoughts :
# 1. By using Greedy Algorithm, We can solve it..!!
# 2. 식의 값을 최소로 만들기 위해서는 -부호가 나타나는 숫자부터 괄호를 열기 시작하여 식이 끝나면 괄호를 닫거나 다음 -부호가 나타나는 숫자 전에서 괄호를 닫아주는 작업을 반복해주면 될 것입니다..!!
# 3. (ex) 55 - (50 + 40)
# 4. 즉, "-"부호를 기준으로 문자열을 분리하여 식의 값을 계산해주면 될 것입니다..!!

import sys

data = sys.stdin.readline().rstrip()

nums = list()
ops = list()

num = ""
for c in data:
    if c == "+" or c == "-":
        nums.append(int(num))
        num = ""
        ops.append(c)
    else:
        num += c
nums.append(int(num))

nums = list(map(str, nums))

data = nums[0]

for i in range(1, len(nums), 1):
    data += ops[i - 1] + nums[i]

# print(data)
# 출력결과 Ex : 9-9

nums = data.split("-")

answer = eval(nums[0])

for i in range(1, len(nums), 1):
    answer -= eval(nums[i])

print(answer)
