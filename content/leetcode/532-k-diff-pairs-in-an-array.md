---
title: 532-K-Diff-Pairs-In-An-Array
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/k-diff-pairs-in-an-array


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
  def findPairs(self, nums: List[int], k: int) -> int:
    ans = 0
    numToIndex = {num: i for i, num in enumerate(nums)}

    for i, num in enumerate(nums):
      target = num + k
      if target in numToIndex and numToIndex[target] != i:
        ans += 1
        del numToIndex[target]

    return ans
```


```
new Solution().findPairs()
```


---
**Score: 5**