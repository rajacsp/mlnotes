---
title: 313-Super-Ugly-Number
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/super-ugly-number


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
  def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
    k = len(primes)
    nums = [1]
    indices = [0] * k

    while len(nums) < n:
      nexts = [0] * k
      for i in range(k):
        nexts[i] = nums[indices[i]] * primes[i]
      next = min(nexts)
      for i in range(k):
        if next == nexts[i]:
          indices[i] += 1
      nums.append(next)

    return nums[-1]
```


```
new Solution().nthSuperUglyNumber()
```


---
**Score: 5**