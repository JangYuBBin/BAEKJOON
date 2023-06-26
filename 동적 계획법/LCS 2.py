# LCS 2, 9252번, 백준

# my thoughts :
# 1. ....

import sys

str1 = sys.stdin.readline().rstrip()
str2 = sys.stdin.readline().rstrip()

len1 = len(str1)
len2 = len(str2)

dp = [[""] * len2 for _ in range(len1)]
# 초깃값 설정
checkFlag = False
for i in range(0, 0 + 1, 1):
    for j in range(0, len2, 1):
        if str1[i] == str2[j]:
            checkFlag = True

            for k in range(j, len2, 1):
                dp[i][k] = str1[i]
            
            break
    
    if checkFlag == True:
        break

checkFlag = False
for i in range(0, len1, 1):
    for j in range(0, 0 + 1, 1):
        if str1[i] == str2[j]:
            checkFlag = True

            for k in range(i, len1, 1):
                dp[k][j] = str2[j]
            
            break
    
    if checkFlag == True:
        break

# print(dp)

for i in range(1, len1, 1):
    for j in range(1, len2, 1):
        if str1[i] == str2[j]:
            dp[i][j] = dp[i - 1][j - 1] + str1[i]
        else:
            if len(dp[i - 1][j]) > len(dp[i][j - 1]):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]

print(len(dp[len1 - 1][len2 - 1]))
print(dp[len1 - 1][len2 - 1])
