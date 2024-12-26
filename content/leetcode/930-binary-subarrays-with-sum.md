---
title: 930-Binary-Subarrays-With-Sum
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/binary-subarrays-with-sum


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
  def numSubarraysWithSum(self, A: List[int], S: int) -> int:
    ans = 0
    prefix = 0
    count = Counter({0: 1})

    for a in A:
      prefix += a
      ans += count[prefix - S]
      count[prefix] += 1

    return ans
```


```
new Solution().numSubarraysWithSum()
```


---
**Score: 5**