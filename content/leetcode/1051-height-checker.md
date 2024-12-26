---
title: 1051-Height-Checker
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/height-checker


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
  def heightChecker(self, heights: List[int]) -> int:
    ans = 0
    currentHeight = 1
    count = [0] * 101

    for height in heights:
      count[height] += 1

    for height in heights:
      while count[currentHeight] == 0:
        currentHeight += 1
      if height != currentHeight:
        ans += 1
      count[currentHeight] -= 1

    return ans
```


```
new Solution().heightChecker()
```


---
**Score: 5**