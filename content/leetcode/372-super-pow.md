---
title: 372-Super-Pow
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/super-pow


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
  def superPow(self, a: int, b: List[int]) -> int:
    def powMod(x: int, y: int) -> int:
      pow = 1
      for _ in range(y):
        pow = (pow * x) % k
      return pow

    k = 1337
    ans = 1

    for i in b:
      ans = powMod(ans, 10) * powMod(a, i) % k

    return ans
```


```
new Solution().superPow()
```


---
**Score: 5**