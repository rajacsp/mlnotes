---
title: 910-Smallest-Range-Ii
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/smallest-range-ii


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
  def smallestRangeII(self, A: List[int], K: int) -> int:
    A.sort()

    ans = A[-1] - A[0]
    left = A[0] + K
    right = A[-1] - K

    for a, b in zip(A, A[1:]):
      mini = min(left, b - K)
      maxi = max(right, a + K)
      ans = min(ans, maxi - mini)

    return ans
```


```
new Solution().smallestRangeII()
```


---
**Score: 5**