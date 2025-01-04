---
title: 217-Contains-Duplicate
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/contains-duplicate


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
  def containsDuplicate(self, nums: List[int]) -> bool:
    return len(nums) != len(set(nums))
```


```
new Solution().containsDuplicate()
```


---
**Score: 5**