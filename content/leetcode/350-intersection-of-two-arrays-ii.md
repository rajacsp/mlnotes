---
title: 350-Intersection-Of-Two-Arrays-Ii
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/intersection-of-two-arrays-ii


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
  def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    if len(nums1) > len(nums2):
      return self.intersect(nums2, nums1)

    ans = []
    count = Counter(nums1)

    for num in nums2:
      if count[num] > 0:
        ans.append(num)
        count[num] -= 1

    return ans
```


```
new Solution().intersect()
```


---
**Score: 5**