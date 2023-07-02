# 셀프 넘버, 4673번, 백준

import sys
from collections import defaultdict

d = defaultdict(list)

for n in range(1, 10_001, 1):
    d_n = n + sum(list(map(int, list(str(n)))))

    d[d_n].append(n)

for n in range(1, 10_001, 1):
    if not d[n]:
        print(n)
