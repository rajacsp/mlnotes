---
title: 1010-Pairs-Of-Songs-With-Total-Durations-Divisible-By-60
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60


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
  def numPairsDivisibleBy60(self, time: List[int]) -> int:
    ans = 0
    count = [0] * 60

    for t in time:
      t %= 60
      ans += count[(60 - t) % 60]
      count[t] += 1

    return ans
```


```
new Solution().numPairsDivisibleBy60()
```


---
**Score: 5**