---
title: 565-Array-Nesting
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/array-nesting


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
  def arrayNesting(self, nums: List[int]) -> int:
    ans = 0

    for num in nums:
      if num == -1:
        continue
      index = num
      count = 0
      while nums[index] != -1:
        temp = index
        index = nums[index]
        nums[temp] = -1
        count += 1
      ans = max(ans, count)

    return ans
```


```
new Solution().arrayNesting()
```


---
**Score: 5**