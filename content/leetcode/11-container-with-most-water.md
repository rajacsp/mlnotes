---
title: 11-Container-With-Most-Water
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/container-with-most-water


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
  def maxArea(self, height: List[int]) -> int:
    ans = 0
    l = 0
    r = len(height) - 1

    while l < r:
      minHeight = min(height[l], height[r])
      ans = max(ans, minHeight * (r - l))
      if height[l] < height[r]:
        l += 1
      else:
        r -= 1

    return ans
```


```
new Solution().maxArea()
```


---
**Score: 5**