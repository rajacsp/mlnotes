---
title: 710-Random-Pick-With-Blacklist
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/random-pick-with-blacklist


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
  def __init__(self, N: int, blacklist: List[int]):
    self.validRange = N - len(blacklist)
    self.dict = {}

    for b in blacklist:
      self.dict[b] = -1

    for b in blacklist:
      if b < self.validRange:
        while N - 1 in self.dict:
          N -= 1
        self.dict[b] = N - 1
        N -= 1

  def pick(self) -> int:
    value = randint(0, self.validRange - 1)

    if value in self.dict:
      return self.dict[value]

    return value
```


```
new Solution().__init__()
```


---
**Score: 5**