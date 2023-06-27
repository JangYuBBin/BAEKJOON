# LCS, 9251번, 백준

# my thoughts :
# 1. By using Dynamic Programming, We can solve it..!!
# 2. dp[i][j] : str1의 i번째 인덱스, str2의 j번째 인덱스까지 확인하였을 때 나올 수 있는 LCS(최장 공통 부분 수열)의 길이
# 3. 결국 우리가 구해야 하는 것은 dp[len(str1) - 1][len(str2) - 1]입니다..!!
# 4. 만약 str1[i] == str2[j]라면 dp[i][j] = dp[i - 1][j - 1] + 1
# 5. 만약 str1[i] != str2[j]라면 dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])입니다..!! <<-- "이 부분은 약간의 센스가 필요했던 것 같습니다..!!"

import sys

str1 = sys.stdin.readline().rstrip()
str2 = sys.stdin.readline().rstrip()

len1 = len(str1)
len2 = len(str2)

dp = [[0] * len2 for _ in range(len1)]
# 초깃값 설정 <<-- "참고로 Dp 배열을 만드는데 있어서 초깃값 설정 작업도 매우 중요한 작업이라고 할 수 있습니다..!!"
checkFlag = False

for i in range(0, 0 + 1, 1):
    for j in range(0, len2, 1):
        if str1[i] == str2[j]:
            checkFlag = True

            for k in range(j, len2, 1):
                dp[i][k] = 1
            
            break
    
    if checkFlag == True:
        break

checkFlag = False

for i in range(0, len1, 1):
    for j in range(0, 0 + 1, 1):
        if str1[i] == str2[j]:
            checkFlag = True

            for k in range(i, len1, 1):
                dp[k][j] = 1
            
            break
    
    if checkFlag == True:
        break

for i in range(1, len1, 1):
    for j in range(1, len2, 1):
        if str1[i] == str2[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        elif str1[i] != str2[j]:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[len1 - 1][len2 - 1])
