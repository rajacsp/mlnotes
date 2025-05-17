---
title: 169-Majority-Element
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/majority-element


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
  def majorityElement(self, nums: List[int]) -> int:
    ans = None
    count = 0

    for num in nums:
      if count == 0:
        ans = num
      count += (1 if num == ans else -1)

    return ans
```


```
new Solution().majorityElement()
```


---
**Score: 5**