---
title: 697-Degree-Of-An-Array
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/degree-of-an-array


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
  def findShortestSubArray(self, nums: List[int]) -> int:
    ans = 0
    degree = 0
    debut = {}
    count = Counter()

    for i, num in enumerate(nums):
      debut.setdefault(num, i)
      count[num] += 1
      if count[num] > degree:
        degree = count[num]
        ans = i - debut[num] + 1
      elif count[num] == degree:
        ans = min(ans, i - debut[num] + 1)

    return ans
```


```
new Solution().findShortestSubArray()
```


---
**Score: 5**