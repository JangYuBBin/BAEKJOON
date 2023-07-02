# 주사위, 1041번, 백준

# my thoughts :
# 1. 틀린 문제이므로 나중에 다시 풀어보아야 할 것 같습니다..!!
# 2. 위 상황의 문제에서 주사위의 면은 1면만 보이거나 2면만 보이거나, 3면이 보이는 경우 밖에 없습니다.
# 3. 또한 각 면이 보이는 개수는 정해져 있습니다.
# 4. 1면이 보이는 개수는 (n - 2)**2 + (n - 2)*(n - 1)*4개
# 5. 2면이 보이는 개수는 4*(n - 2) + 4*(n - 1)개
# 6. 3면이 보이는 개수는 정육면체의 각 꼭짓점으로 4개입니다.
# 7. 이제 각 면의 수가 최소가 되도록 보여주면 되는데 주사위 특성상 마주보는 면을 제외하고 모든 면이 인접해있습니다.
# 8. 따라서 A, B, C, D, E, F를 사용자에게 입력받았을 때 
# 9. A와 F, B와 E, C와 D중 최솟값을 리스트에 저장하고
# 10. 1면, 2면, 3면의 경우에 따라 더 작은 것부터 더해서 사용하면 될 것입니다..!!

import sys

n = int(sys.stdin.readline().rstrip())

nums = list(map(int, sys.stdin.readline().rstrip().split()))

arr = list()

arr.append(min(nums[0], nums[5]))
arr.append(min(nums[1], nums[4]))
arr.append(min(nums[2], nums[3]))

arr.sort()

if n == 1:
    print(sum(nums) - max(nums))
elif n == 2:
    print(4 * (arr[0] + arr[1] + arr[2]) + 4 * (arr[0] + arr[1]))
else:
    answer = 0

    # 1면
    answer += (n - 2)**2 * arr[0] + (n - 2) * (n - 1) * 4 * arr[0]

    # 2면
    answer += 4 * (n - 1) * (arr[0] + arr[1]) + 4 * (n - 2) * (arr[0] + arr[1])

    # 3면
    answer += 4 * (arr[0] + arr[1] + arr[2])

    print(answer)
