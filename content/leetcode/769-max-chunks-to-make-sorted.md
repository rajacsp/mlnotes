---
title: 769-Max-Chunks-To-Make-Sorted
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/max-chunks-to-make-sorted


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
  def maxChunksToSorted(self, arr: List[int]) -> int:
    ans = 0
    maxi = -math.inf

    for i, a in enumerate(arr):
      maxi = max(maxi, a)
      if maxi == i:
        ans += 1

    return ans
```


```
new Solution().maxChunksToSorted()
```


---
**Score: 5**