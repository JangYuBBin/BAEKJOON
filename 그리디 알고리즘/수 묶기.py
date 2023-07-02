# 수 묶기, 1744번, 백준

# my thoughts :
# 1. 일단 길이가 N인 수열을 3개의 그룹으로 분리해야 합니다.
# 2. 1보다 큰 숫자들의 모임
# 3. 1의 모임
# 4. 1보다 작은 수들의 모임
# 5. 1보다 큰 두 수는 곱하는 것이 이득
# 6. 1은 그냥 냅둬서 나중에 더하는 것이 이득
# 7. 0은 음수와 곱하는 것이 이득
# 8. 음수는 서로 곱하는 것이 이득
# 9. 일단 1보다 큰 숫자들을 처리할 때는 내림차순 정렬 후 두 개씩 처리한다. 처리한 수는 clear리스트에 담는다.
# 10. 0개 남으면 완료
# 11. 만약 1개 남으면 그냥 clear리스트에 담는다.
# 12. 이제 1의 모임을 처리해야 한다.
# 13. 1의 모임은 단순하게 그냥 clear리스트에 담으면 된다.
# 14. 이제 마지막으로 1보다 작은 수들을 처리해야 한다.
# 15. 1보다 작은 수들의 모임은 오름차순 정렬한 후 두 개씩 처리한다.
# 16. 마지막에 0개가 남으면 완료
# 17. 마지막에 1개가 남으면 그냥 그대로 clear리스트에 담는다.
# 18. 이제 sum(clear)를 출력하면 될 것이다..!!

import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

arr = list()

for _ in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

plus = list()
one = list()
minus = list() # <<-- "0도 포함..!!"

for val in arr:
    if val > 1:
        plus.append(val)
    elif val == 1:
        one.append(val)
    elif val < 1:
        minus.append(val)

plus.sort(reverse = True)
plus = deque(plus)
minus.sort(reverse = False)
minus = deque(minus)

clear = list()

# 일단 plus 리스트부터 처리합시다..!!
while len(plus) >= 2:
    val1 = plus.popleft()
    val2 = plus.popleft()

    clear.append(val1 * val2)
if not plus:
    pass
elif plus:
    clear.append(plus.popleft())

# 그런다음 one 리스트를 처리합시다..!!
for val in one:
    clear.append(val)

# 마지막으로 minus 리스트를 처리합시다..!!
while len(minus) >= 2:
    val1 = minus.popleft()
    val2 = minus.popleft()

    clear.append(val1 * val2)
if not minus:
    pass
else:
    clear.append(minus.popleft())

print(sum(clear))
