---
title: 179-Largest-Number
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/largest-number


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
class LargerStrKey(str):
  def __lt__(x: str, y: str) -> bool:
    return x + y > y + x


class Solution:
  def largestNumber(self, nums: List[int]) -> str:
    return ''.join(sorted(map(str, nums), key=LargerStrKey)).lstrip('0') or '0'
```


```
new Solution().largestNumber()
```


---
**Score: 5**