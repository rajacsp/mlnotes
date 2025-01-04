---
title: 739-Daily-Temperatures
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/daily-temperatures


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
  def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    ans = [0] * len(temperatures)
    stack = []

    for i, t in enumerate(temperatures):
      while stack and t > temperatures[stack[-1]]:
        index = stack.pop()
        ans[index] = i - index
      stack.append(i)

    return ans
```


```
new Solution().dailyTemperatures()
```


---
**Score: 5**