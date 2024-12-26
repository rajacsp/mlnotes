---
title: 914-X-Of-A-Kind-In-A-Deck-Of-Cards
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards


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
  def hasGroupsSizeX(self, deck: List[int]) -> bool:
    count = Counter(deck)
    return functools.reduce(math.gcd, count.values()) >= 2
```


```
new Solution().hasGroupsSizeX()
```


---
**Score: 5**