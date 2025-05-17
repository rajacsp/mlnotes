---
title: 950-Reveal-Cards-In-Increasing-Order
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/reveal-cards-in-increasing-order


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
  def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
    q = deque()

    for card in reversed(sorted(deck)):
      q.rotate()
      q.appendleft(card)

    return list(q)
```


```
new Solution().deckRevealedIncreasing()
```


---
**Score: 5**