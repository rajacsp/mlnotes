---
title: 611-Valid-Triangle-Number
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/valid-triangle-number


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
  def triangleNumber(self, nums: List[int]) -> int:
    ans = 0

    nums.sort()

    for k in range(len(nums) - 1, 1, -1):
      i = 0
      j = k - 1
      while i < j:
        if nums[i] + nums[j] > nums[k]:
          ans += j - i
          j -= 1
        else:
          i += 1

    return ans
```


```
new Solution().triangleNumber()
```


---
**Score: 5**