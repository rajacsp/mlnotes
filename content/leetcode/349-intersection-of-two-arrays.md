---
title: 349-Intersection-Of-Two-Arrays
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/intersection-of-two-arrays


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
  def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    ans = []
    nums1 = set(nums1)

    for num in nums2:
      if num in nums1:
        ans.append(num)
        nums1.remove(num)

    return ans
```


```
new Solution().intersection()
```


---
**Score: 5**