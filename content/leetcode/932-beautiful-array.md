---
title: 932-Beautiful-Array
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/beautiful-array


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
  def beautifulArray(self, n: int) -> List[int]:
    A = [i for i in range(1, n + 1)]

    def partition(l: int, r: int, mask: int) -> int:
      nextSwapped = l
      for i in range(l, r + 1):
        if A[i] & mask:
          A[i], A[nextSwapped] = A[nextSwapped], A[i]
          nextSwapped += 1
      return nextSwapped - 1

    def divide(l: int, r: int, mask: int) -> None:
      if l >= r:
        return
      m = partition(l, r, mask)
      divide(l, m, mask << 1)
      divide(m + 1, r, mask << 1)

    divide(0, n - 1, 1)
    return A
```


```
new Solution().beautifulArray()
```


---
**Score: 5**