---
title: 560-Subarray-Sum-Equals-K
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/subarray-sum-equals-k


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
  def subarraySum(self, nums: List[int], k: int) -> int:
    ans = 0
    prefix = 0
    count = Counter({0: 1})

    for num in nums:
      prefix += num
      ans += count[prefix - k]
      count[prefix] += 1

    return ans
```


```
new Solution().subarraySum()
```


---
**Score: 5**