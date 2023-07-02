# 멀티탭 스캐쥴링, 1700번, 백준

# my thoughts :
# 1. By using Greedy Algorithm, We can solve it..!!
# 2. 틀린 문제이므로 나중에 다시 풀어보아야 할 것 같습니다.
# 3. 그리디의 기준을 잡는게 까다로웠습니다.
# 4. 처음에는 '지금 시점부터 남은 전기용품의 빈도수'를 기준으로 알고리즘을 택했습니다. 즉 플러그를 뽑아야 할 상황에서는 이후 가장 빈도가 낮은 전기용품의 플러그를 뽑는 식으로 했습니다. 하지만 이런 경우 반례가 생깁니다.
# 5. 따라서 이번에는 남은 전기 용품 리스트에서 가장 나중에 출현하는 전기용품의 플러그를 뽑아보기로 했습니다. 즉 지금 시점부터 남은 전기용품 중 가장 늦게 출현하는 전기용품의 플러그를 뽑는 식으로 알고리즘을 택했습니다.

import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

arr = list(map(int, sys.stdin.readline().rstrip().split()))

multitap = set()

answer = 0 # <<-- "하나씩 플러그를 빼는 최소의 횟수"

for i, val in enumerate(arr):
    if val in multitap:
        continue
    else:
        if len(multitap) < n:
            multitap.add(val)
        elif len(multitap) == n:
            check = list()

            for m in multitap:
                m_idx = len(arr)

                for j in range(i+1, len(arr), 1):
                    if arr[j] == m:
                        m_idx = j
                        break
                
                check.append((m, m_idx))
            
            check.sort(key = lambda x : x[1], reverse = True)

            multitap.remove(check[0][0])
            multitap.add(val)

            answer += 1

print(answer)
