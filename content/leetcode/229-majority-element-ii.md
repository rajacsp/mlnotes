---
title: 229-Majority-Element-Ii
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/majority-element-ii


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
  def majorityElement(self, nums: List[int]) -> List[int]:
    ans1 = 0
    ans2 = 1
    count1 = 0
    count2 = 0

    for num in nums:
      if num == ans1:
        count1 += 1
      elif num == ans2:
        count2 += 1
      elif count1 == 0:
        ans1 = num
        count1 = 1
      elif count2 == 0:
        ans2 = num
        count2 = 1
      else:
        count1 -= 1
        count2 -= 1

    return [ans for ans in (ans1, ans2) if nums.count(ans) > len(nums) // 3]
```


```
new Solution().majorityElement()
```


---
**Score: 5**