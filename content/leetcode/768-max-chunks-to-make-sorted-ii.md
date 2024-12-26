---
title: 768-Max-Chunks-To-Make-Sorted-Ii
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/max-chunks-to-make-sorted-ii


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
    n = len(arr)
    ans = 0
    maxi = -math.inf
    mini = [arr[-1]] * n

    for i in reversed(range(n - 1)):
      mini[i] = min(mini[i + 1], arr[i])

    for i in range(n - 1):
      maxi = max(maxi, arr[i])
      if maxi <= mini[i + 1]:
        ans += 1

    return ans + 1
```


```
new Solution().maxChunksToSorted()
```


---
**Score: 5**