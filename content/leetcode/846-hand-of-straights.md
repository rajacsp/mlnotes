---
title: 846-Hand-Of-Straights
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/hand-of-straights


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
  def isNStraightHand(self, hand: List[int], W: int) -> bool:
    count = Counter(hand)

    for start in sorted(count):
      value = count[start]
      if value > 0:
        for i in range(start, start + W):
          count[i] -= value
          if count[i] < 0:
            return False

    return True
```


```
new Solution().isNStraightHand()
```


---
**Score: 5**