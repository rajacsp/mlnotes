---
title: 219-Contains-Duplicate-Ii
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/contains-duplicate-ii


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
  def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    seen = set()

    for i, num in enumerate(nums):
      if i > k:
        seen.remove(nums[i - k - 1])
      if num in seen:
        return True
      seen.add(num)

    return False
```


```
new Solution().containsNearbyDuplicate()
```


---
**Score: 5**