---
title: 368-Largest-Divisible-Subset
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/largest-divisible-subset


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
  def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
    n = len(nums)
    ans = []
    count = [1] * n
    prevIndex = [-1] * n
    maxCount = 0
    index = -1

    nums.sort()

    for i, num in enumerate(nums):
      for j in reversed(range(i)):
        if num % nums[j] == 0 and count[i] < count[j] + 1:
          count[i] = count[j] + 1
          prevIndex[i] = j
      if count[i] > maxCount:
        maxCount = count[i]
        index = i

    while index != -1:
      ans.append(nums[index])
      index = prevIndex[index]

    return ans
```


```
new Solution().largestDivisibleSubset()
```


---
**Score: 5**