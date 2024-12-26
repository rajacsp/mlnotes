---
title: 996-Number-Of-Squareful-Arrays
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/number-of-squareful-arrays


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
  def numSquarefulPerms(self, A: List[int]) -> int:
    ans = 0
    used = [False] * len(A)

    def isSquare(num: int) -> bool:
      root = int(sqrt(num))
      return root * root == num

    def dfs(path: List[int]) -> None:
      nonlocal ans
      if len(path) > 1 and not isSquare(path[-1] + path[-2]):
        return
      if len(path) == len(A):
        ans += 1
        return

      for i, a in enumerate(A):
        if used[i]:
          continue
        if i > 0 and A[i] == A[i - 1] and not used[i - 1]:
          continue
        used[i] = True
        dfs(path + [a])
        used[i] = False

    A.sort()
    dfs([])
    return ans
```


```
new Solution().numSquarefulPerms()
```


---
**Score: 5**