---
title: 974-Subarray-Sums-Divisible-By-K
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/subarray-sums-divisible-by-k


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
  def subarraysDivByK(self, A: List[int], K: int) -> int:
    ans = 0
    prefix = 0
    count = [1] + [0] * (K - 1)

    for a in A:
      prefix = (prefix + a) % K
      ans += count[prefix]
      count[prefix] += 1

    return ans
```


```
new Solution().subarraysDivByK()
```


---
**Score: 5**