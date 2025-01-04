---
title: 128-Longest-Consecutive-Sequence
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/longest-consecutive-sequence


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
  def longestConsecutive(self, nums: List[int]) -> int:
    ans = 0
    seen = set(nums)

    for num in nums:
      if num - 1 in seen:
        continue
      length = 0
      while num in seen:
        num += 1
        length += 1
      ans = max(ans, length)

    return ans
```


```
new Solution().longestConsecutive()
```


---
**Score: 5**