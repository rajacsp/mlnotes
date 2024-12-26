---
title: 325-Maximum-Size-Subarray-Sum-Equals-K
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/maximum-size-subarray-sum-equals-k


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
  def maxSubArrayLen(self, nums: List[int], k: int) -> int:
    ans = 0
    prefix = 0
    prefixToIndex = {0: -1}

    for i, num in enumerate(nums):
      prefix += num
      target = prefix - k
      if target in prefixToIndex:
        ans = max(ans, i - prefixToIndex[target])
      if prefix not in prefixToIndex:
        prefixToIndex[prefix] = i

    return ans
```


```
new Solution().maxSubArrayLen()
```


---
**Score: 5**