---
title: 66-Plus-One
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/plus-one


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
  def plusOne(self, digits: List[int]) -> List[int]:
    for i, d in reversed(list(enumerate(digits))):
      if d < 9:
        digits[i] += 1
        return digits
      digits[i] = 0

    return [1] + digits
```


```
new Solution().plusOne()
```


---
**Score: 5**