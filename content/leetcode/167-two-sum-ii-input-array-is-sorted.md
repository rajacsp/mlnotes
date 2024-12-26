---
title: 167-Two-Sum-Ii-Input-Array-Is-Sorted
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/two-sum-ii-input-array-is-sorted


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
  def twoSum(self, numbers: List[int], target: int) -> List[int]:
    l = 0
    r = len(numbers) - 1

    while l < r:
      summ = numbers[l] + numbers[r]
      if summ == target:
        return [l + 1, r + 1]
      if summ < target:
        l += 1
      else:
        r -= 1
```


```
new Solution().twoSum()
```


---
**Score: 5**