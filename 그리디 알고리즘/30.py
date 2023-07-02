# 30, 10610번, 백준

# my thoughts :
# 1. 일단 30의 배수이려면 10의 배수이면서 3의 배수이어야 합니다.
# 2. 먼저 10의 배수이려면 일의 자릿수가 0이어야 하고, 3의 배수이려면 모든 자릿수를 더한 수가 3의 배수이어야 합니다.
# 3. 2번을 활용(이용)하여 만들 수 있는 30의 배수 중 가장 큰 수를 만들면 될 것입니다..!!

import sys

nums = list(map(int, list(sys.stdin.readline().rstrip())))

nums.sort(reverse = True)

if nums[-1] == 0:
    if sum(nums) % 3 == 0:
        answer = "".join(list(map(str, nums)))

        print(answer)
    else:
        print(-1)
else:
    print(-1)
