---
title: 556-Next-Greater-Element-Iii
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/next-greater-element-iii


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
  def nextGreaterElement(self, n: int) -> int:
    def nextPermutation(s: List[chr]) -> str:
      i = len(s) - 2
      while i >= 0:
        if s[i] < s[i + 1]:
          break
        i -= 1

      if i >= 0:
        for j in range(len(s) - 1, i, -1):
          if s[j] > s[i]:
            break
        s[i], s[j] = s[j], s[i]

      reverse(s, i + 1, len(s) - 1)
      return ''.join(s)

    def reverse(s: List[chr], l: int, r: int):
      while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1

    s = nextPermutation(list(str(n)))
    ans = int(s)
    return -1 if ans > 2**31 - 1 or ans <= n else ans
```


```
new Solution().nextGreaterElement()
```


---
**Score: 5**