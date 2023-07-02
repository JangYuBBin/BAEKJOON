# 주유소, 13305번, 백준

# my thoughts :
# 1. 일단 제일 왼쪽 도시에서 다음 도시로 가기 위해서 제일 왼쪽 도시에서의 리터당 가격을 이용하여 기름을 넣고 다음 도시로 갑니다.
# 2. 여기서부터가 중요합니다.
# 3. 만약 현재 도시의 리터당 가격이 현재 도시로 오는데 이용한 리터당 가격보다 싸다면 현재 도시의 리터당 가격을 앞으로 이용합니다.
# 4. 만약 현재 도시의 리터당 가격이 현재 도시로 오는데 이용한 리터당 가격보다 비싸다면 계속 이 가격을 이용합니다.
# 5. 이 과정을 반복하면서 맨 오른쪽 도시까지 이동합니다..!!
# 6. 그리디 알고리즘과 관련된 중요한 문제이므로 나중에 다시 풀어보아야 할 것 같습니다..!!

import sys

n = int(sys.stdin.readline().rstrip())

roads = list(map(int, sys.stdin.readline().rstrip().split())) # 도로들
cities = list(map(int, sys.stdin.readline().rstrip().split())) # 도시들

answer = cities[0] * roads[0] # <<-- "일단 다음 도시로 가기위해서 처음 도시에서 리터당 가격을 이용한다."
criterion = cities[0] # <<-- "기준 가격..!! 즉, 현재 도시로 오는데 이용한 리터당 가격이 될 것입니다..!!"

for i in range(1, len(cities) - 1, 1):
    if criterion <= cities[i]:
        answer += criterion * roads[i]
    else:
        criterion = cities[i]
        answer += criterion * roads[i]

print(answer)
