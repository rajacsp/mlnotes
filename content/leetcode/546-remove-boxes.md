---
title: 546-Remove-Boxes
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/remove-boxes


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
  def removeBoxes(self, boxes: List[int]) -> int:
    # Dp(i, j, k) := max score of boxes[i..j] if k boxes equal to boxes[j]
    @functools.lru_cache(None)
    def dp(i: int, j: int, k: int) -> int:
      if i > j:
        return 0

      r = j
      sameBoxes = k + 1
      while r > 0 and boxes[r - 1] == boxes[r]:
        r -= 1
        sameBoxes += 1
      ans = dp(i, r - 1, 0) + sameBoxes * sameBoxes

      for p in range(i, r):
        if boxes[p] == boxes[r]:
          ans = max(ans, dp(i, p, sameBoxes) + dp(p + 1, r - 1, 0))

      return ans

    return dp(0, len(boxes) - 1, 0)
```


```
new Solution().removeBoxes()
```


---
**Score: 5**