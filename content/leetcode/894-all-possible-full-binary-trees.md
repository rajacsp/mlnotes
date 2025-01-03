---
title: 894-All-Possible-Full-Binary-Trees
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/all-possible-full-binary-trees


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
  @functools.lru_cache(None)
  def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
    if n % 2 == 0:
      return []
    if n == 1:
      return [TreeNode(0)]

    ans = []

    for leftCount in range(n):
      rightCount = n - 1 - leftCount
      for left in self.allPossibleFBT(leftCount):
        for right in self.allPossibleFBT(rightCount):
          ans.append(TreeNode(0))
          ans[-1].left = left
          ans[-1].right = right

    return ans
```


```
new Solution().allPossibleFBT()
```


---
**Score: 5**