---
title: 260-Single-Number-Iii
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/single-number-iii


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
  def singleNumber(self, nums: List[int]) -> List[int]:
    xors = functools.reduce(operator.xor, nums)
    lowbit = xors & -xors
    ans = [0, 0]

    # Seperate nums into two groups by the lowbit
    for num in nums:
      if num & lowbit:
        ans[0] ^= num
      else:
        ans[1] ^= num

    return ans
```


```
new Solution().singleNumber()
```


---
**Score: 5**