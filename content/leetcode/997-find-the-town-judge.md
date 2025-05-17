---
title: 997-Find-The-Town-Judge
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/find-the-town-judge


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
  def findJudge(self, n: int, trust: List[List[int]]) -> int:
    count = [0] * (n + 1)

    for a, b in trust:
      count[a] -= 1
      count[b] += 1

    for i in range(1, n + 1):
      if count[i] == n - 1:
        return i

    return -1
```


```
new Solution().findJudge()
```


---
**Score: 5**