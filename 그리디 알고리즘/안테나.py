# 안테나, 18310번, 백준

# my thoughts :
# 1. 틀린 문제이므로 나중에 다시 풀어보아야 할 것 같습니다.
# 2. 수학적으로 생각하면 간단하게 풀 수 있는 문제입니다.
# 3. 모든 집까지의 거리의 총합이 가장 작으려면 일직선 상에서 "가운데"에 가까울수록 총합이 적어집니다.
# 4. 그래서 배열에 집의 위치를 저장하고 정렬 후 중앙값을 찾아서 출력하면 됩니다.

import sys

n = int(sys.stdin.readline().rstrip())

arr = list(map(int, sys.stdin.readline().rstrip().split()))

arr.sort()

print(arr[(n - 1) // 2])
