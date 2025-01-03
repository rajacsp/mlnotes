---
title: 299-Bulls-And-Cows
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/bulls-and-cows


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
  def getHint(self, secret: str, guess: str) -> str:
    bulls = sum(map(operator.eq, secret, guess))
    bovine = sum(min(secret.count(x), guess.count(x)) for x in set(guess))
    return '%dA%dB' % (bulls, bovine - bulls)
```


```
new Solution().getHint()
```


---
**Score: 5**