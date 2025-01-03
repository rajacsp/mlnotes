---
title: 84-Largest-Rectangle-In-Histogram
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/largest-rectangle-in-histogram


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
  def largestRectangleArea(self, heights: List[int]) -> int:
    ans = 0
    stack = []

    for i in range(len(heights) + 1):
      while stack and (i == len(heights) or heights[stack[-1]] > heights[i]):
        h = heights[stack.pop()]
        w = i - stack[-1] - 1 if stack else i
        ans = max(ans, h * w)
      stack.append(i)

    return ans
```


```
new Solution().largestRectangleArea()
```


---
**Score: 5**