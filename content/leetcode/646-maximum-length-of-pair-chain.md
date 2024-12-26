---
title: 646-Maximum-Length-Of-Pair-Chain
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/maximum-length-of-pair-chain


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
  def findLongestChain(self, pairs: List[List[int]]) -> int:
    ans = 0
    prevEnd = -math.inf

    for s, e in sorted(pairs, key=lambda x: x[1]):
      if s > prevEnd:
        ans += 1
        prevEnd = e

    return ans
```


```
new Solution().findLongestChain()
```


---
**Score: 5**