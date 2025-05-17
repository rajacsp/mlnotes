---
title: 830-Positions-Of-Large-Groups
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/positions-of-large-groups


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
  def largeGroupPositions(self, S: str) -> List[List[int]]:
    n = len(S)
    ans = []
    i = 0
    j = 0

    while i < n:
      while j < n and S[j] == S[i]:
        j += 1
      if j - i >= 3:
        ans.append([i, j - 1])
      i = j

    return ans
```


```
new Solution().largeGroupPositions()
```


---
**Score: 5**