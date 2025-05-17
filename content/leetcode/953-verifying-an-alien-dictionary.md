---
title: 953-Verifying-An-Alien-Dictionary
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/verifying-an-alien-dictionary


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
  def isAlienSorted(self, words: List[str], order: str) -> bool:
    dict = {c: i for i, c in enumerate(order)}
    words = [[dict[c] for c in word] for word in words]
    return all(w1 <= w2 for w1, w2 in zip(words, words[1:]))
```


```
new Solution().isAlienSorted()
```


---
**Score: 5**