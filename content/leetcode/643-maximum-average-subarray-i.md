---
title: 643-Maximum-Average-Subarray-I
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/maximum-average-subarray-i


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
  def findMaxAverage(self, nums: List[int], k: int) -> float:
    summ = sum(nums[:k])
    ans = summ

    for i in range(k, len(nums)):
      summ += nums[i] - nums[i - k]
      ans = max(ans, summ)

    return ans / k
```


```
new Solution().findMaxAverage()
```


---
**Score: 5**