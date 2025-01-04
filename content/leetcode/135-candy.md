---
title: 135-Candy
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/candy


```
import pyutil as pyu
pyu.get_local_pyinfo()
```


```
print(pyu.ps2("python-dotenv"))
```


```
from typing import List
```


```
class Solution:
  def candy(self, ratings: List[int]) -> int:
    n = len(ratings)

    ans = 0
    l = [1] * n
    r = [1] * n

    for i in range(1, n):
      if ratings[i] > ratings[i - 1]:
        l[i] = l[i - 1] + 1

    for i in range(n - 2, -1, -1):
      if ratings[i] > ratings[i + 1]:
        r[i] = r[i + 1] + 1

    for a, b in zip(l, r):
      ans += max(a, b)

    return ans
```


```
new Solution().candy()
```


---
**Score: 5**