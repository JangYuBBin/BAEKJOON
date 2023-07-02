# 신입 사원, 1946번, 백준

# my thoughts :
# 1. 일단 (서류심사 성적, 면접시험 성적)순으로 오름차순 정렬한다.
# 2. 자신보다 뒤에 있는 지원자들은 서류심사 성적순위가 무조건 낮기 때문에 고려 대상 x..!!
# 3. 자신보다 앞에 있는 지원자들이 고려 대상입니다..!!
# 4. 리스트를 순회하면서 여태껏 나왔던 성적의 최고 순위를 저장한다.
# 5. 서류심사 성적 순위와 면접시험 성적 순위를 비교하면서 둘 중 하나라도 더 높은 순위가 있다면 통과입니다..!!
# 6. 이 과정을 리스트를 순회하면서 반복해줍니다..!!

import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())

    arr = list()

    for _ in range(n):
        s, m = map(int, sys.stdin.readline().rstrip().split())
        # 참고1 > s : 서류심사 성적 순위
        # 참고2 > m : 면접심사 성적 순위

        arr.append((s, m))
    
    arr.sort(key = lambda x : (x[0], x[1]), reverse = False)

    answer = 1

    best_s = arr[0][0] # -->> "여태껏 나왔던 서류심사 성적 순위의 최고순위"
    best_m = arr[0][1] # -->> "여태껏 나왔던 면접심사 성적 순위의 최고순위"

    for i in range(1, n, 1):
        if best_s > arr[i][0] or best_m > arr[i][1]:
            answer += 1
        
        best_s = min(best_s, arr[i][0])
        best_m = min(best_m, arr[i][1])
    
    print(answer)
