---
title: 334-Increasing-Triplet-Subsequence
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/increasing-triplet-subsequence


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
  def increasingTriplet(self, nums: List[int]) -> bool:
    first = math.inf
    second = math.inf

    for num in nums:
      if num <= first:
        first = num
      elif num <= second:  # First < num <= second
        second = num
      else:
        return True  # First < second < num (third)

    return False
```


```
new Solution().increasingTriplet()
```


---
**Score: 5**