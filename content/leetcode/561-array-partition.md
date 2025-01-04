---
title: 561-Array-Partition
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/array-partition


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
  def arrayPairSum(self, nums: List[int]) -> int:
    return sum(sorted(nums)[::2])
```


```
new Solution().arrayPairSum()
```


---
**Score: 5**