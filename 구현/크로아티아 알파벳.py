# 크로아티아 알파벳, 2941번, 백준

import sys

str = sys.stdin.readline().rstrip()

str = str.replace("c=", "0")
str = str.replace("c-", "0")
str = str.replace("dz=", "0")
str = str.replace("d-", "0")
str = str.replace("lj", "0")
str = str.replace("nj", "0")
str = str.replace("s=", "0")
str = str.replace("z=", "0")

print(len(str))
