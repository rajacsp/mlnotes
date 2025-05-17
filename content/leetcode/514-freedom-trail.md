---
title: 514-Freedom-Trail
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/freedom-trail


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
  def findRotateSteps(self, ring: str, key: str) -> int:
    # Number of rotates of ring to match key[index:]
    @functools.lru_cache(None)
    def dfs(ring: str, index: int) -> int:
      if index == len(key):
        return 0

      ans = math.inf

      # For each ring[i] == key[index]
      # We rotate the ring to match ring[i] w/ key[index]
      # Then recursively match newRing w/ key[index + 1:]
      for i, r in enumerate(ring):
        if r == key[index]:
          minRotates = min(i, len(ring) - i)
          newRing = ring[i:] + ring[:i]
          remainingRotates = dfs(newRing, index + 1)
          ans = min(ans, minRotates + remainingRotates)

      return ans

    return dfs(ring, 0) + len(key)
```


```
new Solution().findRotateSteps()
```


---
**Score: 5**