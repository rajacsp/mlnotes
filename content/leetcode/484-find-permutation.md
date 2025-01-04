---
title: 484-Find-Permutation
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/find-permutation


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
  def findPermutation(self, s: str) -> List[int]:
    ans = []
    stack = []

    for i, c in enumerate(s):
      stack.append(i + 1)
      if c == 'I':
        while stack:  # Consume all decreasings
          ans.append(stack.pop())
    stack.append(len(s) + 1)

    while stack:
      ans.append(stack.pop())

    return ans
```


```
new Solution().findPermutation()
```


---
**Score: 5**