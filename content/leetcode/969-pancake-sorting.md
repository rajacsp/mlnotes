---
title: 969-Pancake-Sorting
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/pancake-sorting


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
  def pancakeSort(self, A: List[int]) -> List[int]:
    ans = []

    for target in range(len(A), 0, -1):
      index = A.index(target)
      A[:index + 1] = A[:index + 1][::-1]
      A[:target] = A[:target][::-1]
      ans.append(index + 1)
      ans.append(target)

    return ans
```


```
new Solution().pancakeSort()
```


---
**Score: 5**